import os
import sys

def checkProject(path):
    project = path.split("/")[0]
    try:
        with open(path, "r") as f:
            lines = f.readlines()
            if "PATH_TO_PROJECT" in lines[0] or "PATH_TO_PROJECT" in lines[1]:
                return (f"{project.title()} PATH_TO_PROJECT is not set in {project}/{project}.config.yaml", 1)
            path = lines[0].split(":")[1].strip()
            path = path[1:-1]
            if not os.path.exists(path):
                return (f"{project.title()} path to training data does not exist", 1)
            path = lines[1].split(":")[1].strip()
            path = path[1:-1]
            if not os.path.exists(path):
                return (f"{project.title()} path to validation data does not exist", 1)
            num_classes = lines[3].split(":")[1].strip()
            if not num_classes.isdigit():
                return (f"{project.title()} num_classes is not an integer", 1)
           
            list_classes = lines[4].split(":")[1][1:-1].split(",")
            if len(list_classes) != int(num_classes):
                return (f"{project.title()} num_classes does not match number of classes", 1)
        print(f"{project.title()} project status: \033[0;32mOK\033[0m.")
        return (f"{project.title()} project is OK.", 0)
    except Exception as e:
        return (f"{project} {e}", 1)

def checkup():
    master_code = 0
    print("Checking up...")
    with open("checkup.log", "w") as f:
        f.write("Checkup begin.\n")
        f.write("----------- DEFECT PROJECT START -----------\n")
        status, code = checkProject(path="defect/defect.config.yaml")
        if code == 1:
            master_code = 1
            f.write(f"STATUS: ERROR\n")
            print("Defect project status: \033[0;31mERROR\033[0m: Check log for details.")
        else:
            f.write(f"STATUS: SUCCESS\n")
        f.write(f"Defect project checkup: {status}\n")
        
        f.write("------------ DEFECT PROJECT END ------------\n")
        f.write("\n----------- PLATE PROJECT START ------------\n")
        status, code = checkProject(path="plate/plate.config.yaml")
        if code == 1:
            master_code = 1
            f.write(f"STATUS: ERROR\n")
            print("Plate project status: \033[0;31mERROR\033[0m: Check log for details.")
        else:
            f.write(f"STATUS: SUCCESS\n")
        f.write(f"Plate project checkup: {status}\n")
        f.write("------------ PLATE PROJECT END -------------\n")
        f.write("Checkup done.\n")
    print("Checkup done.\n")
    return master_code