# Dino-AI
<div align="center">
<img src='https://play-lh.googleusercontent.com/iiIJq5JmLFYNI1bVz4IBHyoXs508JcEzHhOgau69bnveF9Wat51-ax9LMPVOlneKwqg' width='300' >
</div>

## Description
This project is a simple 2D game implemented in Python using the Pygame library, where the player controls a dinosaur character to avoid obstacles (cacti) by jumping over them. What makes this project interesting is that the dinosaur's movements are controlled by a neural network trained using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm.

## NEAT (NeuroEvolution of Augmenting Topologies)
NEAT is a genetic algorithm-based technique for evolving artificial neural networks. It was introduced by Kenneth O. Stanley and others in 2002. NEAT is particularly well-suited for evolving neural networks with complex structures and behaviors.

## Demo

https://github.com/Maciek-Sikora/Dino-AI/assets/43787380/bb02d7be-a4a8-4dcc-a90e-027bc2de344c




## How NEAT Works
1. **Initialization**: NEAT starts with a population of randomly generated neural networks, each representing a potential solution to the given problem.
2. **Evaluation**: Each neural network in the population is evaluated on how well it performs the task (in this case, playing the game). The fitness of each network is determined based on predefined criteria, such as the distance traveled by the dinosaur or the number of obstacles avoided.
3. **Selection**: Networks with higher fitness scores are more likely to be selected for reproduction. NEAT uses a selection method called tournament selection, where networks compete against each other to determine which ones will be chosen as parents for the next generation.
4. **Crossover**: Selected networks undergo crossover (also known as mating), where parts of their genetic material (neural network structure) are combined to create offspring networks. NEAT ensures that offspring networks inherit innovation numbers from their parents, allowing tracking of historical information during evolution.
5. **Mutation**: To introduce diversity and innovation into the population, NEAT applies mutation operators to offspring networks. These mutations can involve adding or removing nodes and connections in the neural network, as well as adjusting connection weights.
6. **Speciation**: NEAT employs speciation to maintain diversity within the population. Networks are grouped into species based on their genetic similarity. During reproduction, NEAT encourages mating within species to preserve specialized behaviors while still allowing for exploration of new solutions.
7. **Repeat**: Steps 2-6 are repeated for multiple generations, gradually improving the population's overall fitness and converging towards better solutions.
By iteratively applying these steps over many generations, NEAT evolves neural networks that are increasingly effective at solving the given task, in this case, playing the game by controlling the dinosaur character.






