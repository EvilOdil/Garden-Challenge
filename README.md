##**How to Setup**##
- Download the codebase as a zip file.
- Extract the files in to a folder
- Open the main.py
- Install pygame 
    ```python
    pip install pygame
    
    ```
- Run the code and check if it is working
- Update the play_area function in main.py to protect the plants.



Here’s a **list of things students can do in the `play_area` function** using the `garden_manager`. These actions allow for plant and pest management, experimentation. Use your coding knowledeg to write an effective play_area function to grow and protect the plantation.

---

## 🌱 **Plant Management**

- **Plant a new seed at a specific location**
    
    ```python
    garden_manager.plant_seed(x=150, y=50)
    
    ```
    

- **Set the plant growth rate**
    
    ```python
    garden_manager.set_growth_rate(1.5)
    
    ```
    
- **Freeze all plants (pause their growth)**
    
    ```python
    garden_manager.freeze_plants()
    
    ```
    
- **Unfreeze all plants**
    
    ```python
    garden_manager.unfreeze_plants()
    
    ```
    
- **Set or increase the maximum plant height**
    
    ```python
    garden_manager.set_max_plant_height(60)
    garden_manager.increase_max_plant_height(10)
    
    ```
    

---

## 🐞 **Pest Management**

- **Remove all pests instantly**
    
    ```python
    garden_manager.remove_all_pests()
    
    ```
    

- **Use bug spray to kill one bug**
    
    ```python
    garden_manager.bug_spray()
    
    ```
    
- **Freeze all bugs for a period**
    
    ```python
    garden_manager.freeze_bugs()  # Freeze for 3 seconds at 60 FPS
    
    ```
    
- **Slow down all bugs**
    
    ```python
    garden_manager.slow_down_pests(factor=0.5)  # Half speed
    
    ```
    

---

## ⏱️ **Game and Timer Management**

- **Get the time left in the game**
    
    ```python
    time_left = garden_manager.get_time_left()
    
    ```
    

---

## 📊 **Score and State Checks**

- **Get the number of living plants**
    
    ```python
    count = garden_manager.get_plant_count()
    
    ```
    
- **Get the number of pests**
    
    ```python
    pest_count = len(garden_manager.pests)
    
    ```
    
- **Check and react to plant or pest conditions**
    
    ```python
    if count < 5:
        garden_manager.plant_seed()
    if pest_count > 3:
        garden_manager.bug_spray()
    
    ```
    

---

## 🧪 **Experimentation Ideas**

- **Change growth rate based on time or events**
    
    ```python
    if time_left < 30:
        garden_manager.set_growth_rate(3.0)
    
    ```
    
- **Automatically plant seeds every few seconds**
    
    ```python
    if timer % (second * 5) == 0:  # Every 5 seconds
        garden_manager.plant_seed()
    
    ```
    
- **Trigger bug spray or freeze when pests are too many**
    
    ```python
    if len(garden_manager.pests) > 5:
        garden_manager.freeze_bugs(frames=120)
    
    ```
    
- **Dynamically adjust max plant height**
    
    ```python
    if timer % (second * 10) == 0:  # Every 10 seconds
        garden_manager.increase_max_plant_height(5)
    
    ```
    

---

## Protect the plants from the Pests!

🥉Protect 30 plants to win the Bronze Medal

🥈Protect 40 plants to win the Silver Medal

🥇Protect 40 plants to win the Gold Medal
