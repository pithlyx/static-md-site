## 📖 Setting Up WSL (Windows Subsystem for Linux)
### ✅ **Compatibility Check**

Before you start, ensure your system is compatible with WSL by verifying the following:

- **Virtualization Enabled in BIOS**
  - Access your BIOS settings (the key varies by manufacturer but is often F2, F10, Delete, or Esc during startup).
  - Look for and enable virtualization settings.
- **WSL Feature Enabled in Windows**
  - Press `Win` + `R`, enter `optionalfeatures`, and hit Enter.
  - Locate and check `Windows Subsystem for Linux`.
  - Click OK and reboot if prompted.
### 🚀 **Initial Installation of WSL**

1. **Open PowerShell as Administrator**
   - Right-click Start, select "Windows PowerShell (Admin)".
2. **Install WSL**
   - Execute: `wsl --install`
   - For a specific Linux distro:
     - List distros: `wsl --list -o`
     - Install chosen distro: `wsl --install -d <distro_name>`
3. **Setup Account**
   - Follow prompts to create a username and password for your Linux distro.
4. **Restart PC**
5. **Access Linux Distro**
   - Open a terminal and type `wsl` to enter your Linux distro.
### 🎛 **WSL Extras**
- **Launch Specific Distro**: `wsl -d <distro>`
- **Set Default Distro**: `wsl -s <Distro>`

## 💻 Setting Up the Terminal
### 🌟 **Windows Terminal**
A modern terminal application that supports multiple tabs, panes, and custom themes.
- **Installation**: Download from the Microsoft Store or GitHub releases page.

### 🖌 **Icons and Fonts**

1. **Download a Font**
   - Visit [Nerd Fonts](https://www.nerdfonts.com/font-downloads).
   - Choose and download your preferred font.
2. **Install Font**
   - Extract and right-click the font file, select "Install".
1. **Update Terminal Font**
   - Apply the new font in Windows Terminal and Visual Studio Code settings.

### 🐚 **ZSH Installation**
ZSH builds on top of the traditional **Bourne shell** adding powerful scripting features, including many features from the typical Linux **Bash** (**B**ourne-**A**gain **SH**ell).

1. **Install ZSH in WSL**
   - Update packages: `$ sudo apt update`
   - Install ZSH: `$ sudo apt install zsh`
   
2. **Install Oh My Zsh**
   - Oh My Zsh is a framework for Zsh, the Z shell, which enhances the shell's capabilities with themes, plugins, and convenient features. To install it, run the following command in your terminal:`sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
   - This script will install Oh My Zsh and change your default shell to Zsh. If you are prompted to switch to Zsh during installation, confirm with `Y`.

3. **Switching Shells with ZSH**
   - The following commands allow you to switch between Zsh and Bash shells:
     - Nest shell: `$ zsh` (opens a Zsh session within the current shell)
     - Replace shell: `$ exec zsh` (replaces the current shell session with Zsh)
   - To return to Bash from Zsh, you can similarly run `$ exec bash`.

4. **Customizing Oh My Zsh**
   - Oh My Zsh comes with numerous themes and plugins. You can customize your Zsh configuration by editing the `~/.zshrc` file.
   - For example, to change your theme 
	   - Example themes: [top-12-themes](https://travis.media/top-12-oh-my-zsh-themes-for-productive-developers/) [best-looking-themes](https://randomtechs.com/best-looking-ohmyzsh-themes/)


## 🌐 Node.js and npm via NVM
NVM allows you to manage multiple versions of Node.js and npm easily.

1. **Install NVM**
   - In WSL, run: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash`
2. **Restart Shell**
   - Close and reopen your terminal or source your profile.
3. **Install Node.js (Includes npm)**
   - Execute: `nvm install node`