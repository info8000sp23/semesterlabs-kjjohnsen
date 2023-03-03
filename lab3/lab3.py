
def process_name(name:str):
    parts = name.split(",") # handle comma separated names
    if len(parts) == 2: #this will only be the case if they used a comma
        return parts[1].strip(),parts[0].strip()
    parts = name.split(" ") # now spaces might be the delimiter
    if len(parts) == 1: # handle a single word
        return parts[0].strip(),"unknown"
    return (" ".join(parts[0:-1])).strip(),parts[-1].strip() # the normal case

def process_gender(gender:str):
    return gender[0].lower()

def process_age(age:str):
    try:
        return int(age)
    except:
        return -1
    
def process_height(height:str):
    height = int(height)
    if height < 100:
        return height,"in"
    return height,"cm"

def process_line(line:str):
    parts = line.split(";")
    first,last = process_name(parts[0])

    issue = 0
    if last == "unknown":
        issue = 1
        
    gender = process_gender(parts[1])
    email = parts[2]
    age = process_age(parts[3])

    if age == -1:
        issue = 1

    height,probable_unit = process_height(parts[4])
    weight = int(parts[5].strip())

    if probable_unit=="in":
        height = height*2.54
        weight = round(weight*0.453592)
        issue = 1

    return [first,last,email,gender,age,height,weight,issue]

with open("data/messy.ssv") as f:
    lines = f.readlines()

print(len(lines),lines)


#now we need to get 8 lists
first_names = []
last_names = []
emails = []
ages = []
genders = []
heights = []
weights = []
issues = []

for line in lines:

    fields = process_line(line)
    email = fields[2]
    try: # find the email and delete it
        index = emails.index(email)
        del first_names[index]
        del last_names[index]
        del emails[index]
        del genders[index]
        del ages[index]
        del heights[index]
        del weights[index]
        del issues[index]
    except ValueError: # better to except a specific error rather than all of them
        pass 

    first_names.append(fields[0])
    last_names.append(fields[1])
    emails.append(fields[2])
    genders.append(fields[3])
    ages.append(fields[4])
    heights.append(fields[5])
    weights.append(fields[6])
    issues.append(fields[7])

print(first_names)
print(last_names)
print(emails)
print(ages)
print(genders)
print(heights)
print(weights)
print(issues)
print(len(emails))

# part 2, processing

# first, replace any -1 ages with the median age
import numpy as np
good_ages = [x for x in ages if x > 0]
median_age = round(np.median(good_ages))
print(median_age)
imputed_indices = []
correct_indices = []
for index,age in enumerate(ages):
    if age == -1:
        imputed_indices.append(index) 
        ages[index] = median_age
    else:
        correct_indices.append(index)
print(ages)

# next, compute bmi
bmis=[]
for index,_ in enumerate(emails):
    height_m = heights[index]/100
    bmi = weights[index]/(height_m*height_m)
    bmis.append(round(bmi,1))
print(bmis)

# now we re-export as clean.ssv
with open("data/clean.ssv","w") as f:
    for i,email in enumerate(emails):
        line_to_write = ";".join([str(x) for x in [emails[i],first_names[i],last_names[i],genders[i],ages[i],heights[i],weights[i],bmis[i],issues[i]]])
        f.write(line_to_write+"\n")

# Now we visualize
import matplotlib.pyplot as plt
fig,axs = plt.subplots(1,2,figsize=(10,5))

# first we do a scatter plot.  The hard part here (in theory) in splitting up the lists.  
axs[0].plot([ages[i] for i in imputed_indices],[bmis[i] for i in imputed_indices],"r+",label="imputed")
axs[0].plot([ages[i] for i in correct_indices],[bmis[i] for i in correct_indices],"b*",label="correct")
axs[0].set_xlabel("age (years)")
axs[0].set_ylabel("bmi ($kg/m^2$)") # note the use of latex
axs[0].set_title("Age by BMI")
axs[0].legend()

# No we do the bar chart
# dictionaries work well for this because we'll have to index by genders, which is a string
underweights = {'m':0,'f':0,'n':0}
healthyweights = {'m':0,'f':0,'n':0}
overweights = {'m':0,'f':0,'n':0}
for gender,bmi in zip(genders,bmis):
    if bmi < 18.5:
        underweights[gender]+=1
    elif bmi > 24.9:
        overweights[gender]+=1
    else:
        healthyweights[gender]+=1

axs[1].bar(x=[0,1,2],height=underweights.values(),label="underweight")
axs[1].bar(x=[4,5,6],height=healthyweights.values(),label="normal")
axs[1].bar(x=[8,9,10],height=overweights.values(),label="overweight")
axs[1].set_xticks([0,1,2,4,5,6,8,9,10])
axs[1].set_xticklabels(['Male','Female','Non-Binary']*3,rotation='vertical')
axs[1].set_title("Count of BMI categories by reported gender")
axs[1].legend()
plt.tight_layout()
fig.savefig('figure.png',bbox_inches='tight')

# last but not least, generate the "pretty printed" table
import pandas as pd
df = pd.read_csv("data/clean.ssv",delimiter=";")
df.columns = ['email','first_name','last_name','gender','age','height_cm','weight_kg','bmi','issues']
issue_people = df[df.issues==1]
print(issue_people)

# I like things to be autogenerated, so I'm going to write my readme in this file

with open("readme.md","w") as readme:
    readme.write(
f'''# Lab 3

My Figure:

![](figure.png)

My Table:
{issue_people.to_html()}

'''
)