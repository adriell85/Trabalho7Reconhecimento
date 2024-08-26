import matplotlib
matplotlib.use('TkAgg')
from runs import KNNRuns,DMCRuns,BayesianGaussianDiscriminantRuns,KmeansQuantRuns, BayesianRejectionRuns,BayesianGaussianMixtureRuns


def main():
    BayesianGaussianMixtureRuns(0)
    BayesianGaussianMixtureRuns(1)
    BayesianGaussianMixtureRuns(2)
    BayesianGaussianMixtureRuns(3)

if __name__ == "__main__":
    main()
