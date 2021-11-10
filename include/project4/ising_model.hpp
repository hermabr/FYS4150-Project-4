#pragma once

#include <vector>
#include <random>
#include <iostream>

// temporary because of exp-function
#include <cmath>

using namespace std;
class IsingModel{
    public:
        IsingModel(int L, double T);
        vector<vector<int>> get_spins();
        // Performs one Monte Carlo cycle of Metropolis algorithm and
        // Updates energy- and magnetization-values.
        void metropolis();
        // Should only be called by constructor, but kept public as it might be useful
        // for debugging later.
        void set_energy();
        int get_energy();
        // Should only be called by constructor, but kept public as it might be useful
        // for debugging later.
        void set_magnetisation();
        int get_magnetisation();
        void print();
    private:
        // Called by constructor to initialise 2D vector of spins.
        // (currently a placeholder-function that sets every other spin equal to -1)
        void initialize_spins(int L);
        mt19937 rng;
        uniform_int_distribution<int> rand_index;
        uniform_int_distribution<int> rand_1_or_0;
        uniform_real_distribution<double> uniform;
        vector<vector<int>> spins;
        int L;
        int E;
        int M;
        double beta;
};