from travellingSalesmanGeneticAlgorithm import TravellingSalesmanGeneticAlgorithm

if __name__ == "__main__":
    trvl_slsmn_genetic_algorithm: TravellingSalesmanGeneticAlgorithm = TravellingSalesmanGeneticAlgorithm(20)
    gens_200: float = trvl_slsmn_genetic_algorithm.find_shortest_path(200, 20)
    print(gens_200)