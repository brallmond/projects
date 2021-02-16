#!/bin/bash
#needs arguments reps, speed 
#must let script finish to get cursor back

DEFAULT_REPS=5
DEFAULT_SPEED=10
reps=${1:-$DEFAULT_REPS}
speed=${2:-$DEFAULT_SPEED}
tput civis #turns cursor invisible
for ((i=0;i<reps;i++)){ # repeats left to right motion

for ((j=0;j<6;j++)){ # right motion
  printf '\r'; # carriage return
  for ((k=0;k<j;k++)){ # spaces in front of char
    printf ' ';
  }; 
  printf "\e[48;5;$((j+16))m \e[0m"; # colored char
  sleep $((1000*1 / speed))e-3; # time between movements of colored char
}; 

for ((j=0;j<6;j++)){ # left motion
  printf '\r\e[2K'; #carriage return and line clear
  for ((k=5-j;k>0;k--)){
    printf ' ';
  };
  printf "\e[48;5;$((21-j))m \e[0m";
  sleep $((1000*1 / speed))e-3;
};

}
tput cnorm #makes cursor visible again
echo
