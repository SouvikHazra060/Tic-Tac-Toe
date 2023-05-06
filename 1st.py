# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:52:20 2023

@author: SOUVIK
"""

def Constboard(board):
  print("\n\nCurrent state of Board\n\n");
  for i in range(0,9):
    if((i>0) and (i%3)==0):
      print("\n");
    if(board[i]==0):
      print("_ ", end=" ");
    if(board[i]==-1):
      print("X " ,end=" ");
    if(board[i]==1):
      print("O ", end=" ");
      
     
      
def User1Turn(board):
    pos=int(input("\nEnter X position from (1 to 9): "));
    if(board[pos-1]!=0):
        print("\nWrong Move!!");
        exit(0);
    board[pos-1]=-1;

def User2Turn(board):
    pos=int(input("\nEnter O position from (1 to 9): "));
    if(board[pos-1]!=0):
        print("\nWrong Move!!");
        exit(0);
    board[pos-1]=1;
    
def minmax(board, player):
    x=analyzeboard(board);
    if(x!=0):
        return (x*player);
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player;
            score=-minmax(board, player*-1);
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
    if(pos==-1):
        return 0;
    return value;
        
def Compturn(board):
       pos=-1;
       value=-2;
       for i in range(0,9):
           if(board[i]==0):
               board[i]=1;
               score=-minmax(board, -1);
               board[i]=0;
               if(score>value):
                   value=score;
                   pos=i;
       board[pos]=1;         

    
def analyzeboard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    for i in range(0,8):
        if((board[cb[i][0]]!=0) and (board[cb[i][0]]== board[cb[i][1]]) and (board[cb[i][0]]==board[cb[i][2]])):
            return board[cb[i][0]];    
    return 0;  


def main():
    choice=input("Enter 1 for single player || Enter 2 for multiplayer :--\n");
    choice=int(choice);
    board=[0,0,0,0,0,0,0,0,0]
    if(choice==1):
        print("\nMatch b/w Computer(O) vs You(X)\n ");
        player=int(input("\nChoose whether you want to play 1st or 2nd :--"));
        for i in range(0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i+player)%2==0): 
                Constboard(board);
                Compturn(board);
            else:
               Constboard(board);
               User1Turn(board);
               
    else:
         for i in range(0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i%2)==0):
               Constboard(board);
               User1Turn(board);
            else:
               Constboard(board);
               User2Turn(board);
               
    x=analyzeboard(board);
    if(x==0):
        Constboard(board);
        print("\n\nDraw!!");
    if(x==-1):
        Constboard(board);
        print("\n\nPlayer X win|| O loose");            
    if(x==1):
        Constboard(board);
        print("\n\nPlayer O win|| X loose");
               
               