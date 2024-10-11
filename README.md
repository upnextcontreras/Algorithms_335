# Couple Swapping Algorithms

This repository contains three algorithms aimed at solving the "Couples Holding Hands" problem. Each algorithm minimizes the number of swaps required to ensure that all couples are sitting next to each other in a given row.

## Problem Description

Given an array `row` where row[i] is the id of the person sitting in the i-th seat, the people are arranged in pairs, and we need to ensure that couples (represented by consecutive integers) are seated next to each other. The goal is to minimize the number of swaps required to achieve this.

## Algorithms

### Algorithm 1: Connection Pairs of Persons

This algorithm minimizes the number of swaps by using a dictionary to map the position of each person in the row and then iteratively swapping people to ensure that couples are next to each other.

#### Algorithm Outline:

1. **Create a Map of Positions**: 
   - The algorithm starts by creating a dictionary (`index_map`) that maps each person's ID to their index in the row.
   
2. **Iterate Through the Row in Pairs**:
   - The algorithm iterates through the row two elements at a time.
   - For each pair, it checks whether the second person is the correct partner (using XOR operation to find the partner).
   
3. **Swap If Necessary**:
   - If the correct partner is not sitting next to the first person, the algorithm finds the partner using the `index_map` and swaps them with the current second person.
   
4. **Update the Map**:
   - After each swap, the `index_map` is updated to reflect the new positions of the swapped individuals.
   
5. **Track the Number of Swaps**:
   - A counter is maintained to track the number of swaps performed.

### Algorithm 2: Greedy Approach to Hamiltonian Problem

### Algorithm 3: Ensuring Convenient Schedules

