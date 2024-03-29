import java.util.Arrays;
import java.util.List;

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

    public static int getPopulation(List<Country> countries, String continent) {
        int p = 0;
        for (Country c : countries) {
            if (c.getContinent().equals(continent)) {
                p += c.getPopulation();
            }
        }
        return p;
    }

    public static void main(String[] args) {
        List<Country> countries = Arrays.asList(
                new Country("China"),
                new Country("DPRK"),
                new Country("Korea"),
                new Country("Japan"));
        String continent = "5";
        int p = getPopulation(countries, continent);
        System.out.println(p);
    }
}
