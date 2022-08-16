alias v='nvim'
alias x='startx'
alias l='ls -al --color=auto'
alias ls='ls --color=auto'
export CHROME_EXECUTABLE='chromium'
export PATH="${PATH}:/home/david/.cargo/bin:/home/david/flutter/bin:/home/david/android-studio/bin:/home/david/.local/bin:/home/david/bin"
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
export _JAVA_OPTIONS="-Djogl.disable.openglcore=false -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true"

BLUE="\[$(tput setaf 4)\]"
RESET="\[$(tput sgr0)\]"

PS1="${BLUE}\w${RESET}> "
