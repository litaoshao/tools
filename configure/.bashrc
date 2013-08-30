# trash
mkdir -p ~/.trash
alias rm=trash
alias r=trash
alias rl='ls ~/.trash'
alias ur=undelfile
alias ct=cleartrash
undelfile()
{
  mv -i ~/.trash/$@ ./
}
trash()
{
  mv $@ ~/.trash/
}

cleartrash()
{
    read -p "clear sure?[n]" confirm
    [ $confirm == 'y' ] || [ $confirm == 'Y' ]  && /bin/rm -rf ~/.trash/*
}

function g { 
    case $1 in
        mysvn) cd ~/workspace/mysvn/ ;;
        workspace) cd ~/workspace ;;
        online) cd ~/online/mysvn ;;
    esac
}

