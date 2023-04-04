# Changelog

## Viikko 3

- Sovelluksen alustus; yhdistetty tietokanta ja luotu tietokantataulu projekteille
- Luotu ProjectRepository-luokka, jonka tehtävänä on projektien tallennus, poisto ja haku tietokannasta
- Luotu ProjectService-luokka, jonka tehtävänä on ProjectRepositoryn metodien kutsuminen ja sovelluslogiikka
- Luotu ProjectListView jossa projektit haetaan ProjectServicen avulla ja listataan käyttäjälle, sekä ProjectView joka sisältää listauksen sekä käyttöliittymän uuden projektin luomiseen
- Luotu TestProjectRepository, joka testaa projektien hakemista ja uusien tehtävien luomista
