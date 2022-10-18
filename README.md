# Algorithme_Genetique

# Projet IA: Star Wars
## Tatouine en danger
Dans la bordure extérieure, un satellite non identifié à eté repéré dans le ciel autour de la plaète Tatouine se déplaçant en orbite hauteà très grande vitesse constante. Les analystes de l’alliance sont sur le coup. Ce satellite ne répond à aucune injonction; le premier probème est d’éviter toute collision entre ce satellite et la flotte de satellites de l’alliance déjà en opération. Mais surtout, il s’agit de se préparer à une destruction imminente du satellite par un tir de plasma pulsé.
Malheureusement, au sol, l’énergie nécessaire à son atomisation est trop limitée et un seul tir sera possible. Vous n’avez donc pas le droit à l’erreur. Il va falloir préparer ce tir au mieux avec les rares moyens disponibles.
Le satellite suit une orbite dîte de Lissajous1 définit comme suit: 

x(t)=p1 ×sin(p2 ×t+p3)

y(t)=p4 ×sin(p5 ×t+p6)

Avec x(t) et y(t) la position du satellite à un instant t donnée. Les pi, i ∈ [1; 6] sont les paramètres qu’il va falloir découvrir afin de pouvoir anticiper au mieux les mouvements du satellite à un instant t donné (t ∈ [0; 2π]).
A l’aide de lunettes à visée laser, la rébellion a pu relever avec une certaine précision la position du satellite à plusieurs instants. Cette liste vous est fournie dans le fichier position sample.csv .
