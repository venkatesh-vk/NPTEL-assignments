stats = dict()
LINE= input()
while LINE:
      (wsets,lsets,wgames,lgames) = (0,0,0,0)

      (WINNER  ,LOSER ,setscores) = LINE.strip().split(':',2)

      sets = setscores.split(',')
      for set in sets:
      
          (winstr,losestr) = set.split('-')
          win = int(winstr)
          lose = int(losestr)
          wgames = wgames +win
          lgames = lgames+ lose
          if win > lose:
              wsets = wsets+1
          else:
              lsets=lsets+1
      for player in [WINNER  ,LOSER ]:
          try:
              stats[player]
          except KeyError:
              stats[player]=[0,0,0,0,0,0]
      if wsets >=3:
          stats[WINNER  ][0]=stats[WINNER  ][0]+1
      else:
          stats[WINNER  ][1]=stats[WINNER  ][1]+1
      stats[WINNER  ][2]=stats[WINNER  ][2]+ wsets
      stats[WINNER  ][3]=stats[WINNER  ][3]+wgames
      stats[WINNER  ][4]=stats[WINNER  ][4]-lsets
      stats[WINNER  ][5]=stats[WINNER  ][5] - lgames
      stats[LOSER ][2] = stats[LOSER ][2] + lsets
      stats[LOSER ][3] = stats[LOSER ][3] + lgames
      stats[LOSER ][4] = stats[LOSER ][4]  - wsets
      stats[LOSER ][5] = stats[LOSER ][5]  - wgames
      LINE = input()
statlist = [(stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],name) for name in
stats.keys() for stat in [stats[name]]]

statlist.sort(reverse = True)

for e in statlist:
      print(e[6],e[0],e[1],e[2],e[3],-e[4],-e[5])
