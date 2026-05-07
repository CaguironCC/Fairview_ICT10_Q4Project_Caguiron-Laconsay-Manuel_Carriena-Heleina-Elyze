from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
absences_data = [0, 0, 0, 0, 0]


def add_absence(e):
   day = document.getElementById("day").value
   absence = document.getElementById("absence").value
  
   if absence == "":
       document.getElementById("output").innerHTML = "Please enter a number."
       return
  
   absence = int(absence)
   if absence < 0:
       absence = 0
  
   index = days.index(day)
   absences_data[index] = absence
   document.getElementById("output").innerHTML = f"{day} updated with {absence} absences."


def show_graph(e):
   document.getElementById("graph").innerHTML = ""
   plt.close()
  
   x = np.array(days)
   y = np.array(absences_data)
  
   plt.figure(figsize=(8, 5))
   plt.plot(x, y, marker="o", linestyle="-", linewidth=2, markersize=8, color="#2c7da0")
   plt.title("Weekly Attendance (Absences)", fontsize=14, fontweight="bold")
   plt.xlabel("Days of the week", fontsize=11)
   plt.ylabel("Number of Absences", fontsize=11)
   plt.grid(True, alpha=0.3, linestyle="--")
   plt.tight_layout()
  
   display(plt, target="graph")
   document.getElementById("output").innerHTML = "Graph has been generated."


class cs:
   def __init__(self, name, section, subject):
       self.name = name
       self.section = section
       self.subject = subject


   def introduce(self):
       return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.subject}."


classmates = [
   cs("Balagat, Michael", "10-Sapphire", "Science"),
   cs("Bernardo, Miko", "10-Sapphire", "Math"),
   cs("Caguiron, Carriena", "10-Sapphire", "Social Studies"),
   cs("Calida, Lorenzo", "10-Sapphire", "English"),
   cs("Chan, Jazmar", "10-Sapphire", "PE"),
   cs("Cruz, Rohann", "10-Sapphire", "Science"),
   cs("David, Terd", "10-Sapphire", "Social Studies"),
   cs("De Guzman, Nia", "10-Sapphire", "Science"),
   cs("De Guzman, Uno", "10-Sapphire", "Math"),
   cs("Francisco, Annika", "10-Sapphire", "PE"),
   cs("Kaur, Nav", "10-Sapphire", "Math"),
   cs("Laconsay, Heleina", "10-Sapphire", "English"),
   cs("Lepasana, Khen", "10-Sapphire", "PE"),
   cs("Lopez, Liam", "10-Sapphire", "Math"),
   cs("Lucman, Mohammad", "10-Sapphire", "Science"),
   cs("Malapitan, Caleb", "10-Sapphire", "Art"),
   cs("Manahan, Samantha", "10-Sapphire", "Science"),
   cs("Manuel, Elyze", "10-Sapphire", "Math"),
   cs("Mendoza, Matthew", "10-Sapphire", "PE"),
   cs("Palafox, Coby", "10-Sapphire", "PE"),
   cs("Ramirez, Alfiona", "10-Sapphire", "Math"),
   cs("Reynoso, Izeck", "10-Sapphire", "Music"),
   cs("Santos, Cas", "10-Sapphire", "PE"),
   cs("Santos, Rafa", "10-Sapphire", "Social Studies"),
   cs("Tolentino, Kelsey", "10-Sapphire", "English"),
   cs("Toribio, Sasha", "10-Sapphire", "English"),
   cs("Valdez, David", "10-Sapphire", "Science")
]


def add(e):
   name = document.getElementById("new-name").value
   section = document.getElementById("new-section").value
   subject = document.getElementById("new-subject").value
  
   if not name:
       return
  
   if not section:
       section = "10-Sapphire"
   if not subject:
       subject = "N/A"
  
   classmates.append(cs(name, section, subject))
  
   show(e)
  
   document.getElementById("new-name").value = ""
   document.getElementById("new-section").value = ""
   document.getElementById("new-subject").value = ""
   document.getElementById("add-panel").style.display = "none"


def show(e):
   container = document.getElementById("dynamic-classlist")
   container.innerHTML = ""
  
   for c in classmates:
       container.innerHTML += f"""
       <div class="classmate-entry">
           {c.introduce()}
       </div>
       """


def show_panel(e):
   document.getElementById("add-panel").style.display = "block"


def hide_panel(e):
   document.getElementById("add-panel").style.display = "none"
   document.getElementById("new-name").value = ""
   document.getElementById("new-section").value = ""
   document.getElementById("new-subject").value = ""


from js import window


if "classmates" in window.location.pathname:
   show(None)
   document.getElementById("add-classmate-btn").onclick = show_panel
   document.getElementById("confirm-add").onclick = add
   document.getElementById("cancel-add").onclick = hide_panel


