# Reinforcement Learning (RL)
## Om RL
- Målet med RL är att träna en maskin så att den kan förstå sin *environment* så att den kan göra *actions* som maximerar den långsiktiga *rewarden*.  
- En *Agent* experimenterar genom att ta olika beslut och observera resultaten. Systemet (agenten) kommer att bli bättre och bättre på att fatta beslut allteftersom erfareheten ökar.
- *Policys* beskriver AI-agentens "kunskap"
- Markov Decision Process (MDP) är en viktig del i Reinforcement Learning. I konceptet antas också att man har att göra med diskreta "units of time", tex turns i ett spel eller liknande.
### Fem principer för RL:
1. Input / output system  
- *Inputs* representerar *environment*, dvs i vilket *state" systemet befinner sig.<br>
- *Outputs* är de *actions* som AI-modellen (*agenten*) beslutar att den ska ta.<br>
- *Policys* är de "regler" som systemet har för att fatta sina besluta. Det är dessa plicys som tränas när man tränar modellen.<br>
<img src="bilder\20241220_064603730_iOS.png" alt="Alt Text" width="600" height="250">
<br>
  
2. Rewards
- *Rewards* är en metric som anger hur bra systemet fungerar, som en feedback på den *action* som Agenten tog i förra steget.
- Målet är att maximera gains och minimera förluster
- Rewards kan vara short term eller long term (cumulative)
- Generellt vill man maximera long term rewards
3. Environment
- *Environment* är den miljön i vilken systemet opererar
- Källan till information om *state* och *reward*
- "rules of the game"
- rewards witch each posible action
4. Markov Decision Process (MDP)
- Matematisk beslutsprocess
- Discrete units of time
- Flöde:
    - Observera systemets nuvarande state S vid tiden t, St
    - Ta action a vid tiden t, at
    - Få en reward vid tiden t, rt
    - enter next step
<br>
<img src="bilder\20241220_071057157_iOS.png" alt="Alt Text" width="600" height="250">
<br>
5. Training Mode vs Inference Mode
- I *training mode* lär sig systemet. Systemet uppdaterar och optimerar sin *policy*.
- I *inference mode* använder systemets sina *policys*. Systemet är full-lärt.  

## Q-Learning
- Q-learning är en undergrupp till Reinforcement Learning
- En *AI-agent* opererar i en *environment* med *states* och *rewards* ("inputs") och *actions* ("outputs").
- AI-agenten försöker konstruera en optimal policy, genom att interagera med miljön, den använder "trial and error"-metodik.
- AI-agenten använder inte en underliggande matematisk modell, utan den försöker optimera sina policies genom att direkt interagera med miljön. (Thompson sampling har mer en underliggande modell?)
### Principer för Q-Learning
- Q-Learning har samma principer som RL generellt (se ovan), samt utöver det två ytterligare principer:
1. Antalet möjliga states är begränsat (="observation space")
2. Antalet olika actions är begränsat (="action space")

### Q-värden
- Q-värden indikerar "quality" av en action (a), givet ett state (s): Q(s, a)
- Q-värden är nuvarande estimat av summan av alla framtida rewards

### Q-tables
- Q-värden sparas i en Q-table och dess värden representerar AI-agentens *policy*
- Varje möjligt state finns som en rad
- Varje möjlig action i varje state, finns i en kolumn, exempel med "cliff":
<br>
<img src="bilder\\cliff_q_values.png" alt="Alt Text" width="400" height="250">
<br>
<img src="bilder\\q_table.png" alt="Alt Text" width="400" height="250">
<br>

## Länkar
[YT: Dr Daniel Soper, Foundations of reinforcement learning](https://www.youtube.com/watch?v=wVXXLLT6srY)  
[YT: Dr Daniel Soper, Foundations of Q-Learning](https://www.youtube.com/watch?v=__t2XRxXGxI&t=30s)  
[YT: Dr Daniel Soper, A complete example in Python](https://www.youtube.com/watch?v=iKdlKYG78j4&t=6s)