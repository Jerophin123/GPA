#!/bin/bash

# Define colors and reset color
SKY_BLUE="\033[1;36m"
GREEN="\033[1;32m"
RED="\033[1;31m"
RESET="\033[0m"

# Print the letters in different colors
echo -e "${SKY_BLUE}                                                               "
echo -e "                                                               "
echo -e "IIIIIIIIII   ${GREEN}MMMMMMMM               ${RED}MMMMMMMM           CCCCCCCCCCCCC"
echo -e "${SKY_BLUE}I::::::::I   ${GREEN}M:::::::M             ${RED}M:::::::M        CCC::::::::::::C"
echo -e "${SKY_BLUE}I::::::::I   ${GREEN}M::::::::M           ${RED}M::::::::M      CC:::::::::::::::C"
echo -e "${SKY_BLUE}II::::::II   ${GREEN}M:::::::::M         ${RED}M:::::::::M     C:::::CCCCCCCC::::C"
echo -e "${SKY_BLUE}  I::::I     ${GREEN}M::::::::::M       ${RED}M::::::::::M    C:::::C       CCCCCC"
echo -e "${SKY_BLUE}  I::::I     ${GREEN}M:::::::::::M     ${RED}M:::::::::::M   C:::::C              "
echo -e "${SKY_BLUE}  I::::I     ${GREEN}M:::::::M::::M   ${RED}M::::M:::::::M   C:::::C              "
echo -e "${SKY_BLUE}  I::::I     ${GREEN}M::::::M M::::M ${RED}M::::M M::::::M   C:::::C              "
echo -e "${SKY_BLUE}  I::::I     ${GREEN}M::::::M  M::::M${RED}::::M  M::::::M   C:::::C              "
echo -e "${SKY_BLUE}  I::::I     ${GREEN}M::::::M   M:::::::M   M::::::M   C:::::C              "
echo -e "${SKY_BLUE}  I::::I     ${GREEN}M::::::M    M:::::M    M::::::M   C:::::C              "
echo -e "${SKY_BLUE}  I::::I     ${GREEN}M::::::M     MMMMM     M::::::M    C:::::C       CCCCCC"
echo -e "${SKY_BLUE}II::::::II   ${GREEN}M::::::M               ${RED}M::::::M     C:::::CCCCCCCC::::C"
echo -e "${SKY_BLUE}I::::::::I   ${GREEN}M::::::M               ${RED}M::::::M      CC:::::::::::::::C"
echo -e "${SKY_BLUE}I::::::::I   ${GREEN}M::::::M               ${RED}M::::::M        CCC::::::::::::C"
echo -e "${SKY_BLUE}IIIIIIIIII   ${GREEN}MMMMMMMM               ${RED}MMMMMMMM           CCCCCCCCCCCCC"
echo -e "                                                               "
echo -e "                                                               "
echo -e "                                                               ${RESET}"

# Launch the Python script
gunicorn app_mob:app


