class Country {
    private String continent;
    private int population;

    public Country(String name) {
        continent = String.valueOf(name.length());
        population = 1000;
    }

    public String getContinent() {
        return continent;
    }

    public int getPopulation() {
        return population;
    }
}
