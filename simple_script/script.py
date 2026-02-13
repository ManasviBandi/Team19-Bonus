import os
import re

defaultFile = "examples/default/model/car.drawio" 
output = "examples/default/src-gen" 

os.makedirs(output, exist_ok=True)

with open(defaultFile, "r") as file:
    for line in file:
        # skip edgeLabel, must be vertex with text
        if line.find('vertex="1"') != -1 and line.find('value=') != -1 and line.find('edgeLabel') == -1:
            start = line.find('value="') + 7
            end = line.find('"', start)
            # no whitespaces
            className = line[start:end].split('<')[0].strip() 

            # when saying the class name only should be letters, numbers, underscores
            className = re.sub(r'[^0-9a-zA-Z_]', '', className)

            # drives1 keeps making a class -> not supposed to
            if className == "":
                continue

            if className[0].isalpha():
                # create java file path
                classPath = os.path.join(output, f"{className}.java")
                with open(classPath, "w") as classFile:
                    # basic class 
                    classFile.write(f"public class {className} {{\n}}\n")
print("Done!")