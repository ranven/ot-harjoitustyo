<h1>Vaatimusm&auml;&auml;rittely</h1>

<p>Sovellus on ToDo-sovellus, jonka tarkoitus on auttaa käyttäjäänsä projektien ja niihin liittyvien tehtävien hallinnassa. Käyttäjä voi sovelluksen avulla pitää kirjaa eri projekteistaan ja tehtävistään, ja seurata projektiensa edistymistä.</p>

<h2>K&auml;ytt&auml;j&auml;t</h2>

<p>Sovelluksella on yksi k&auml;ytt&auml;j&auml;rooli <em>(normaali k&auml;ytt&auml;j&auml;).</em> Sovelluksessa ei ole kirjautumistoiminnallisuutta.</p>

<h2>Perustoiminnallisuudet</h2>

<p>Toiminnallisuudet voi karkeasti jakaa kahteen luokkaan: projekteihin ja teht&auml;viin. Luodut projektit ja teht&auml;v&auml;t talletetaan SQLite-tietokantaan.</p>

<h4>Projektit:</h4>

<ul>
	<li>K&auml;ytt&auml;j&auml; voi luoda projektin, jonka sis&auml;lle tallennetaan todo-teht&auml;vi&auml;</li>
	<li>K&auml;ytt&auml;j&auml; voi n&auml;hd&auml; luomansa projektit avatessaan sovelluksen</li>
	<li>K&auml;ytt&auml;j&auml; voi editoida projektin nime&auml;</li>
	<li>K&auml;ytt&auml;j&auml; voi poistaa projektin</li>
	<li>Klikkaamalla projektia k&auml;ytt&auml;j&auml; voi n&auml;hd&auml; projektiin liittyv&auml;t teht&auml;v&auml;t listana</li>
    <li>Käyttäjä voi projektinäkymässä nähdä suoritettujen tehtävien määrän ja kokonaismäärän tehtävistä jokaisen projektin osalta.</li>
</ul>

<h4>Teht&auml;v&auml;t:</h4>

<ul>
	<li>K&auml;ytt&auml;j&auml; voi n&auml;hd&auml; luomansa teht&auml;v&auml;t listana avatessaan projektin</li>
	<li>K&auml;ytt&auml;j&auml; voi luoda uuden teht&auml;v&auml;n projektin sis&auml;lle</li>
	<li>K&auml;ytt&auml;j&auml; voi m&auml;&auml;ritt&auml;&auml; teht&auml;v&auml;lle nimen, kuvauksen sek&auml; prioriteetin (1-5)</li>
	<li>K&auml;ytt&auml;j&auml; voi poistaa teht&auml;v&auml;n</li>
	<li>K&auml;ytt&auml;j&auml; voi merkit&auml; teht&auml;v&auml;n tehdyksi</li>
	<li>K&auml;ytt&auml;j&auml; voi vaihtaa n&auml;kym&auml;n n&auml;ytt&auml;m&auml;&auml;n vain tehdyt / vain tekem&auml;tt&ouml;m&auml;t teht&auml;v&auml;t</li>
</ul>

<h2>Lis&auml;toiminnallisuudet / jatkokehitysideat:</h2>

<ul>
	<li>K&auml;ytt&auml;j&auml; voi valita miss&auml; j&auml;rjestyksess&auml; luodut teht&auml;v&auml;t listataan (prioriteettij&auml;rjestys, aikaj&auml;rjestys, aakkosj&auml;rjestys)</li>
	<li>Luotujen teht&auml;vien editoiminen</li>
    <li>Projektin edistymisen seuranta</li>
	<li>Statistiikkasivu, jossa k&auml;ytt&auml;j&auml; voi n&auml;hd&auml; tietoja projekteista/teht&auml;vist&auml; (ulkoista kirjastoa hy&ouml;dynt&auml;en)</li>
	<li>Kun projektin jokainen teht&auml;v&auml; on tehty, k&auml;ytt&auml;j&auml; voi n&auml;hd&auml; projektin&auml;kym&auml;ss&auml; projektin merkittyn&auml; valmiiksi</li>
	<li>Aikarajan asettaminen teht&auml;ville</li>
	<li>(Vaatii aikarajan) desktop-notifikaatiot kun teht&auml;v&auml; on saavuttamassa aikarajaansa</li>
	<li>Export-toiminnallisuus, joka tallentaa kaikki luodut projektit ja teht&auml;v&auml;t esim. tekstitiedostoksi</li>
	<li>Integraatio Googlen rajapintojen kanssa, kuten teht&auml;v&auml;n aikarajan vieminen Google Calendar-APIn kautta omaan kalenteriin tai teht&auml;vien vieminen Sheets APIn kautta excel-tiedostoon</li>
</ul>
