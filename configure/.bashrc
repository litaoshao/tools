# trash
mkdir -p /search/.trash
alias rm=trash  
alias r=trash  
alias rl='ls /search/.trash'
alias ur=undelfile
alias ct=cleartrash
undelfile()
{
  mv -i /search/.trash/$@ ./
}
trash()
{
  mv $@ /search/.trash/
}

cleartrash()
{
    read -p "clear sure?[n]" confirm
    [ $confirm == 'y' ] || [ $confirm == 'Y' ]  && /bin/rm -rf /search/.trash/*
}

function g { 
    case $1 in
        mysvn) cd /search/workspace/mysvn/ ;;
        workspace) cd /search/workspace ;;
        online) cd /search/online/mysvn ;;
    esac
}

