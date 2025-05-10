<template>
  <v-app>
    <div class="app">
      <!-- Header -->
      <header class="header" v-if="!isMobile">
        <h1 id="logo">KupiVozi 🚗</h1>
        <v-card style="width: 100%; max-width: 50vw; margin: 0 auto;">
          <template v-slot:text>
            <v-text-field
              v-model="search"
              label="Search"
              prepend-inner-icon="mdi-magnify"
              variant="outlined"
              hide-details
              single-line
              theme="dark"
            ></v-text-field>
          </template>
        </v-card>
        <div class="pagination" v-if=!isMobile>
          <button @click="prevPage" :disabled="currentPage === 1">Претходно</button>
          <span>Page {{ currentPage }} of {{ totalPages }}</span>
          <button @click="nextPage" :disabled="currentPage === totalPages">Следно</button>
        </div>
      </header>

      <header class="header" style="justify-content: center; align-items: center" v-if="isMobile">
        <h1 id="logo">KupiVozi 🚗</h1>
      </header>

      <v-card style="width: 100%; max-width: 90vw; margin: 10px auto;" v-if="isMobile">
          <template v-slot:text>
            <v-text-field
              v-model="search"
              label="Search"
              prepend-inner-icon="mdi-magnify"
              variant="outlined"
              hide-details
              single-line
              theme="dark"
            ></v-text-field>
          </template>
        </v-card>

      <div class="main-content">
        <!-- Филтри -->
        <v-dialog v-model="showFiltersDialog" fullscreen hide-overlay transition="dialog-bottom-transition" v-if="isMobile">
          <template v-slot:activator="{ props }">
            <v-btn v-bind="props" class="collapsible">Филтри</v-btn>
          </template>
          <v-card>
            <v-toolbar>
              <v-btn icon @click="showFiltersDialog = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Филтри</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <h3>Филтри</h3>
              <v-select
                clearable
                label="Бренд"
                :items="brands"
                v-model="filteredBrands"
                placeholder="Одбери бренд"
                variant="solo"
              ></v-select>
              <v-select
                clearable
                label="Модел"
                :items="availableModels"
                v-model="filteredModels"
                placeholder="Одбери модел"
                variant="solo"
                no-data-text="Немате изберено бренд"
              ></v-select>
              <h3>Цена</h3>
              <div class="price-range">
                <v-text-field
                  v-model="filters.priceRange[0]"
                  density="compact"
                  type="number"
                  variant="outlined"
                  hide-details
                  single-line
                ></v-text-field>
                <span>-</span>
                <v-text-field
                  v-model="filters.priceRange[1]"
                  density="compact"
                  type="number"
                  variant="outlined"
                  hide-details
                  single-line
                ></v-text-field>
              </div>
              <v-range-slider
                v-model="filters.priceRange"
                step="500"
                :min="priceMin"
                :max="priceMax"
                :ripple="false"
              ></v-range-slider>
              <h3>Година</h3>
              <v-select
                label="Година од"
                :items="godiniPod"
                v-model="filters.yearFrom"
                variant="outlined"
              ></v-select>
              <v-select
                label="Година до"
                :items="godiniNad"
                v-model="filters.yearTo"
                variant="outlined"
              ></v-select>
              <h3>Екстра</h3>
              <v-select
                clearable
                label="Менувач"
                :items="transmissions"
                v-model="filters.transmission"
                placeholder="Одбери менувач"
              ></v-select>
              <v-select
                clearable
                label="Гориво"
                :items="fuelTypes"
                v-model="filters.fuelType"
              ></v-select>
              <v-select
                clearable
                label="Регистрација"
                :items="registrationTypes"
                v-model="filters.registration"
              ></v-select>

              <button @click="resetFilters">Ресетирај</button>
            </v-card-text>
          </v-card>
        </v-dialog>

        <aside class="sidebar" v-if="!isMobile">
          <div class="content" :class="{ show: showFilters }">
            <h3>Филтри</h3>
            <v-select
              clearable
              label="Бренд"
              :items="brands"
              v-model="filteredBrands"
              placeholder="Одбери бренд"
              variant="solo"
            ></v-select>
            <v-select
              clearable
              label="Модел"
              :items="availableModels"
              v-model="filteredModels"
              placeholder="Одбери модел"
              variant="solo"
              no-data-text="Немате изберено бренд"
            ></v-select>
            <h3>Цена</h3>
            <div class="price-range">
              <v-text-field
                v-model="filters.priceRange[0]"
                density="compact"
                type="number"
                variant="outlined"
                hide-details
                single-line
                class="fixniSe"
              ></v-text-field>
              <v-text-field
                v-model="filters.priceRange[1]"
                density="compact"
                type="number"
                variant="outlined"
                hide-details
                single-line
                ></v-text-field>
            </div>
            <v-range-slider
              v-model="filters.priceRange"
              step="500"
              :min="priceMin"
              :max="priceMax"
              style="width: 90%; margin: auto;"
              ></v-range-slider>
            <h3>Година</h3>
            <v-select
              label="Година од"
              :items="godiniPod"
              v-model="filters.yearFrom"
              variant="outlined"
            ></v-select>
            <v-select
              label="Година до"
              :items="godiniNad"
              v-model="filters.yearTo"
              variant="outlined"
            ></v-select>
            <h3>Екстра</h3>
            <v-select
              clearable
              label="Менувач"
              :items="transmissions"
              v-model="filters.transmission"
              placeholder="Одбери менувач"
            ></v-select>
            <v-select
              clearable
              label="Гориво"
              :items="fuelTypes"
              v-model="filters.fuelType"
            ></v-select>
            <v-select
              clearable
              label="Регистрација"
              :items="registrationTypes"
              v-model="filters.registration"
            ></v-select>

            <button @click="resetFilters">Ресетирај</button>
          </div>
        </aside>

        <!-- Car List Section -->
        <section class="car-list" style="overflow-y: auto; max-height: 70vh;" v-if="search === ''">
          <div class="card-grid">
            <div v-for="car in paginatedCars" :key="car.id" class="car-card">
              <img :src="car.image" alt="Car image" />
              <div class="car-info">
                <span class="car-name" @click="openCarLink(car.link)">
                  {{ car.brand }} {{ car.model }} ({{ car.year }})
                </span>
                <span class="car-price">{{ car.price }}€</span>
                <div class="car-details">
                  <span>{{ car.transmission }} ● {{ car.fuelType }} ● {{ car.mileage }}km</span>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="car-list" style="overflow-y: auto; max-height: 70vh;" v-else>
          <div class="card-grid">
            <div v-for="car in searchAll" :key="car.id" class="car-card">
              <img :src="car.image" alt="Car image" />
              <div class="car-info">
                <span class="car-name" @click="openCarLink(car.link)">
                  {{ car.brand }} {{ car.model }} ({{ car.year }})
                </span>
                <span class="car-price">{{ car.price }}€</span>
                <div class="car-details">
                  <span>{{ car.transmission }} ● {{ car.fuelType }}</span>
                </div>
              </div>
            </div>
          </div>
        </section>
        <div class="pagination" v-if=isMobile>
          <button @click="prevPage" :disabled="currentPage === 1">Претходно</button>
          <span>Page {{ currentPage }} of {{ totalPages }}</span>
          <button @click="nextPage" :disabled="currentPage === totalPages">Следно</button>
        </div>
      </div>
    </div>
  </v-app>
</template>


<script setup>
import { ref, computed, onMounted, watch} from 'vue'
import Papa from 'papaparse'

const showFilters = ref(true)
const priceMin = 0
const priceMax = 25000
const yearMin = 1980
const yearMax = 2025

const filters = ref({
  //se koristat za filter na kolite (ne e vizuelno)
  brand: null,
  model: null,
  priceRange: [priceMin, priceMax],
  yearFrom: yearMin,
  yearTo: yearMax,
  transmission: null,
  fuelType: null,
  registration: null,
  link: null,
  mileage: null,
})

const brands = [ "Audi", "BMW", "Mercedes", "Volkswagen", "Citroen", "Peugeot", "Fiat", "Opel",
  "-------------",
  "Alfa Romeo", "Abarth", "Bentley", "BYD", "Cadillac", "Chevrolet", "Chrysler",
  "Dacia", "Daewoo", "Daihatsu", "Dodge", "DS", "Ford", "Honda", "Hummer", "Hyundai",
  "Isuzu", "Jaguar", "Jeep", "Kia", "Lada", "Lancia", "Land Rover", "Lexus",
  "Maserati", "Mazda", "Mini", "Mitsubishi", "Nissan", "Renault", "Seat", "Skoda",
  "Smart", "SsangYong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volvo", "Yugo",
  "Zastava"]
const models = {
  'BMW': [
    "1-серии (сите)", "114", "116", "118", "120", "123", "125", "128", "130",
    "135", "140", "2-серии (сите)", "214", "216", "218", "220", "225", "228",
    "230", "235", "240", "3-серии (сите)", "315", "316", "318", "320", "323",
    "324", "325", "328", "330", "335", "340", "Active Hybrid 3", "4-серии (сите)",
    "418", "420", "425", "428", "430", "435", "440", "5-серии (сите)", "518",
    "520", "523", "524", "525", "528", "530", "535", "540", "545", "550",
    "Active Hybrid 5", "6-серии (сите)", "620", "628", "630", "633", "635", "645",
    "650", "7-серии (сите)", "725", "728", "730", "732", "735", "740", "745",
    "750", "760", "Active Hybrid 7", "8-серии (сите)", "830", "840", "850",
    "i3", "i8", "i4", "i5", "i7", "iX", "iX1", "iX2", "iX3", "M-серии (сите)",
    "M 1", "M 2", "M 3", "M 4", "M 5", "M 6", "M 8", "Active Hybrid x6",
    "X-серии (сите)", "X 1", "X 2", "X 3", "X 4", "X 7", "XM", "X 5", "X 6",
    "Z-серии (сите)", "Z 1", "Z 3", "Z 4", "Z 8"],
  'Mercedes': [
    "190", "200", "208", "210/310", "220", "230", "240", "250", "260", "270",
    "280", "290", "300", "308", "320", "350", "380", "400", "416", "420", "450",
    "500", "560", "600", "А-класа (сите)", "AMG ONE", "A 140", "A 150", "A 160",
    "A 170", "A 180", "A 190", "A 200", "A 210", "A 220", "A 250", "A 35 AMG",
    "A 45 AMG", "Actros", "AMG GT", "Atego", "B-класа (сите)", "B 150", "B 160",
    "B 170", "B 180", "B 200", "B 220", "B 250", "B Electric Drive", "C-класа (сите)",
    "C 160", "C 180", "C 200", "C 220", "C 230", "C 240", "C 250", "C 270", "C 280",
    "C 300", "C 30 AMG", "C 320", "C 32 AMG", "C 350", "C 36 AMG", "C 400", "C 43 AMG",
    "C 450", "C 55 AMG", "C 63 AMG", "CE-класа (сите)", "CLE 180", "CLE 200",
    "CLE 220", "CLE 300", "CLE 450", "CLE 53 AMG", "CLE 63 AMG", "CE 200", "CE 220",
    "CE 230", "CE 280", "CE 300", "Citan", "CL-класа (сите)", "CL 160", "CL 180",
    "CL 200", "CL 220", "CL 230", "CL 420", "CL 500", "CL 55 AMG", "CL 600",
    "CL 63 AMG", "CL 65 AMG", "CLA-класа (сите)", "CLA  180", "CLA  200", "CLA  220",
    "CLA  250", "CLA 35 AMG", "CLA  45 AMG", "CLC-класа (сите)", "CLC 160", "CLC 180",
    "CLC 200", "CLC 220", "CLC 230", "CLC 250", "CLC 350", "CLK-класа (сите)",
    "CLK 200", "CLK 220", "CLK 230", "CLK 240", "CLK 270", "CLK 280", "CLK 320",
    "CLK 350", "CLK 430", "CLK 500", "CLK 55 AMG", "CLK 63 AMG", "CLS-класа (сите)",
    "CLS 220", "CLS 250", "CLS 280", "CLS 300", "CLS 320", "CLS 350", "CLS 400",
    "CLS 500", "CLS 55 AMG", "CLS 63 AMG", "E-класа (сите)", "E 200", "E 220",
    "E 230", "E 240", "E 250", "E 260", "E 270", "E 280", "E 290", "E 300", "E 320",
    "E 350", "E 36 AMG", "E 400", "E 420", "E 430", "E 43 AMG", "E 50", "E 500",
    "E 53 AMG", "E 55", "E 60 AMG", "E 63 AMG", "EQC-400 Klasse", "EQA", "EQA 250",
    "EQA 300", "EQB 200", "EQB 300", "EQB 350", "EQC 400", "EQE 300", "EQE 350",
    "EQE 43", "EQE SUV", "EQS", "EQS SUV", "EQT", "EQV 250", "EQV 300", "G-класа (сите)",
    "G 230", "G 240", "G 250", "G 270", "G 280", "G 290", "G 300", "G 320", "G 350",
    "G 400", "G 500", "G 55 AMG", "G 63 AMG", "G 65 AMG", "S 560", "S 580",
    "GL-класа (сите)", "GL 320", "GL 350", "GL 420", "GL 450", "GL 500", "GL 55 AMG",
    "GL 63 AMG", "GLA-класа (сите)", "GLA 180", "GLA 200", "GLA 220", "GLA 250",
    "GLA 45 AMG", "GLB-класа (сите)", "GLB 180", "GLB 200", "GLB 220", "GLB 250",
    "GLA 35 AMG", "GLB 35 AMG", "GLC-класа (сите)", "GLC 220", "GLC 250", "GLC 300",
    "GLC 350", "GLC 400", "GLC 450", "GLE 300", "GLC 43 AMG", "GLC 63 AMG",
    "GLE-класа (сите)", "GLE 250", "GLE 350", "GLE 400", "GLE 43 AMG", "GLE 450",
    "GLE 500", "GLE 53 AMG", "GLE 63 AMG", "GLE 58", "GLK-класа (сите)", "GLK 200",
    "GLK 220", "GLK 250", "GLK 280", "GLK 300", "GLK 320", "GLK 350", "GLS-класа (сите)",
    "GLS 350", "GLS 400", "GLS 500", "GLS 63 AMG", "GLS 580", "GLS 600", "MB 100",
    "ML-класа (сите)", "ML 230", "ML 250", "ML 270", "ML 280", "ML 300", "ML 320",
    "ML 350", "ML 400", "ML 420", "ML 430", "ML 450", "ML 500", "ML 55 AMG", "ML 63 AMG",
    "ML Marco polo", "R-класа (сите)", "R 280", "R 300", "R 320", "R 350", "R 500",
    "R 63 AMG", "S-класа (сите)", "S 250", "S 260", "S 280", "S 300", "S 320", "S 350",
    "S 400", "S 420", "S 430", "S 450", "S 500", "S 55", "S 55 AMG", "S 550", "S 600",
    "S 63 AMG", "S 65 AMG", "S 650", "S 680", "SL-класа (сите)", "SL 230", "SL 250",
    "SL 280", "SL 300", "SL 320", "SL 350", "SL 380", "SL 420", "SL 450", "SL 500",
    "SL 55 AMG", "SL 560", "SL 600", "SL 60 AMG", "SL 63 AMG", "SL 65 AMG", "SL 70 AMG",
    "SL 73 AMG", "SL 43 AMG", "SL 55 AMG", "SLC-класа (сите)", "SLC 180", "SLC 200",
    "SLC 250", "SLC 280", "SLC 300", "SLC 43 AMG", "SLC 380", "SLC 450", "SLC 500",
    "SLK-класа (сите)", "SLK 200", "SLK 230", "SLK 250", "SLK 280", "SLK 300",
    "SLK 320", "SLK 32 AMG", "SLK 350", "SLK 55 AMG", "SLR", "SLS AMG", "Sprinter",
    "T1", "T2", "V-класа (сите)", "V 200", "V 220", "V 230", "V 280", "Vaneo", "Vario",
    "Viano", "Vito", "X-Klass 220", "X-Klass 250", "X-Klass 350", "V 300"],
  'Audi': ["100", "200", "80", "90", "А-класа (сите)", "А1", "A2", "A3", "A4", "A5",
    "A6", "А7", "A8","Q 1", "Q 2", "Q 3", "Q 4 -etron", "Q 5", "Q 6", "Q 7", "Q 8", "Q 8 e-tron",
    "RS e-tron GT", "RS Q2", "RS Q3", "RS Q5", "RS", "RS 2", "R 8", "SQ7",
    "RS 3", "RS 4", "RS 5", "RS 6", "RS 7", "S-класа (сите)", "S1", "S2", "S3",
    "S4", "S5", "S6", "S7", "S8", "SQ2", "SQ3", "SQ5", "SQ6", "SQ8", "SQ8 e-tron",
    "TT", "TT RS", "TTS", "V8"],
  'Volkswagen (VW)': ["181", "Amarok", "Anfibio", "Arteon", "Altos", "Beetle", "Bora", "Buggy",
    "Caddy", "Coccinelle", "Corrado", "Crafter", "Cros Touran", "Derby",
    "e-up!", "Eos", "Escarabajo", "Fox", "Golf", "Golf Plus", "ID. Buzz", "ID.3",
    "ID.4", "ID.5", "ID.6", "ID.7", "Iltis", "Jetta", "Kafer", "Karmann Ghia",
    "Kever", "L 80", "LT", "Lupo", "Maggiolino", "New Beetle", "Passat", "Passat CC",
    "Phaeton", "Pointer", "Polo", "Routan", "Santana", "Scirocco", "Sharan", "T1",
    "T2", "T3 Други", "T3 Caravelle", "T3 Multivan", "T4 Други", "T4 Caravelle",
    "T4 Multivan", "T5 Други", "T5 Caravelle", "T5 Multivan", "T5 Shuttle",
    "T6 California", "T6 Caravelle", "T6 Multivan", "T6 Transporter", "T7 Transporter",
    "T-Cross", "T-Roc", "Taigo", "Taro", "Tayron", "Tiguan", "Touareg", "Touran",
    "Transporter", "up!", "Vento", "Viloran", "XL1"],
  'Citroen': ["Acadiane", "Ami", "AX", "Axel", "Berlingo", "BX", "C-Crosser",
    "C-Elysee", "C-Zero", "C1", "C15", "C2", "C25", "C3", "C3 Aircross",
    "C3 Picasso", "C35", "C4", "C4 Picasso", "C4 Cactus", "C4 Aircross",
    "C4 Space Tourer", "Grand C4 Picasso", "Grand C4 Picasso Space Tourer",
    "C4 X", "C5", "C5 Aircross", "C5 X", "C6", "C8", "C-Crosse", "CX", "DS",
    "DS3", "DS4", "DS5", "Dyane", "E-Mehari", "Evasion", "GSA", "Jumper",
    "Jumpy", "LNA", "Mehari", "Holidays", "Nemo", "SAXO", "SM", "Spacetourer",
    "Traction", "Visa", "Xantia", "XM", "Xsara", "Xsara Picasso", "ZX"],
  'Peugeot': ["1007", "104", "106", "107", "108", "2008", "204", "205", "206", "207",
    "208", "3008", "301", "304", "305", "306", "307", "308", "309", "4007",
    "4008", "404", "405", "406", "407", "5008", "504", "505", "508", "408",
    "604", "605", "607", "806", "807", "Bipper", "Boxer", "Expert", "iOn",
    "J5", "J9", "Partner", "RCZ", "Rifter", "Traveller"],
  'Renault': ["Alpine A110", "Alpine A310", "Alpine A610", "Alaskan", "Arkana", "Austral",
    "Rafale", "Symbioz", "Avantime", "Captur", "Clio", "Espace", "Express",
    "Fluence", "Fuego", "Grand Espace", "Grand Modus", "Grand Scenic", "Kadjar",
    "Kangoo", "Koleos", "Laguna", "Latitude", "Logan", "Master", "Megane",
    "Modus", "R 11", "R 14", "R 18", "R 19", "R 20", "R 21", "R 25", "R 30",
    "R 4", "R 5", "R 6", "R 9", "Safrane", "Sandero", "Sandero Stepway",
    "Scenic", "Spider", "Symbol", "Talisman", "Trafic", "Twingo", "Twizy",
    "Vel Satis", "Wind", "ZOE"],
  'Seat': ["Arona", "Alhambra", "Ateca", "Altea", "Altea XL", "Tarraco", "Arosa", "Cordoba", "Exeo", "Ibiza", "Inca", "Leon", "Malaga", "Marbella", "Mii", "Mii Electric", "Terra", "Toledo"],
  'Fiat': ["124", "126", "127", "128", "130", "131", "132", "133", "500",
    "500C", "500L", "500X", "595", "600", "Barchetta", "Brava", "Bravo",
    "Cinquecento", "Coupe", "Croma", "Doblo", "Ducato", "Fiorino", "Grande Punto",
    "Grande Punto Abarth", "Idea", "Linea", "Marea", "Multipla", "Panda",
    "Punto", "Qubo", "Scudo", "Sedici", "Seicento", "Spider Europa", "Stilo",
    "Strada", "Talento", "Tempra", "Tipo", "Ulysse", "Uno"],
  'Opel': ["Adam", "Agila", "Ampera", "Antara", "Ascona", "Astra", "Calibra", "Cavalier",
    "Combo", "Cascada", "Commodore", "Corsa", "Crossland", "Frontera", "Grandland",
    "GT", "Insignia", "Kadett", "Karl", "Manta", "Meriva", "Mokka", "Monza",
    "Movano", "Omega", "Rekord", "Senator", "Signum", "Speedster", "Tigra",
    "Vectra", "Vivaro", "Zafira"],
  'Skoda': ["Citigo", "Enyaq", "Fabia", "Favorit", "Felicia", "Kodiaq", "Kamiq", "Octavia", "Rapid", "Roomster","Scala", "Superb", "Yeti","Karoq"],
  'Alfa Romeo': ["145", "146", "147", "149", "155", "156", "159", "164", "166", "33",
    "4C", "75", "8C", "90", "6", "Alfasud", "Alfetta", "Brera", "Giulia",
    "Giulietta", "GT", "GTV", "MiTo", "Montreal", "Spider", "Stelvio", "Tonale"],
  'Ford': ["Aerostar", "B-Max", "Bronco", "C-Max", "Capri", "Cougar", "Courier",
    "Econoline", "EcoSport", "Edge", "Escape", "Escort", "Excursion",
    "Expedition", "Explorer", "F-150", "F-250", "F-350", "Fiesta", "Focus",
    "Fusion", "Galaxy", "Granada", "GT", "Ka", "Kuga", "Maverick", "Mondeo",
    "Mustang", "Orion", "Probe", "Puma", "Ranger", "Scorpio", "Sierra",
    "S-Max", "Taurus", "Thunderbird", "Tourneo", "Transit"],
  'Chevrolet': ["Alero", "Astro", "Avalanche", "Aveo", "Bel Air", "Beretta", "Blazer", "Bolt",
    "Camaro", "Caprice", "Captiva", "Cavalier", "Corvette", "Cruze", "El Camino",
    "Epica", "Equinox", "Evanda", "Express", "HHR", "Impala", "Kalos", "Lacetti",
    "Lumina", "Malibu", "Matiz", "Monte Carlo", "Niva", "Nubira", "Orlando",
    "Silverado", "Spark", "Suburban", "Tahoe", "Trailblazer", "Traverse", "Trax",
    "Volt"],
  'Toyota': ["4-Runner", "Auris", "Avalon", "Avensis", "Aygo", "C-HR", "bZ4X", "Camry",
    "Carina", "Celica", "Corolla", "Crown", "FJ", "Hiace", "Highlander", "Hilux",
    "IQ", "Land Cruiser", "MR 2", "Paseo", "Picnic", "Prius", "RAV 4", "Sequoia",
    "Sienna", "Starlet", "Supra", "Tacoma", "Tercel", "Tundra", "Urban Cruiser",
    "Verso", "Yaris"],
  'Kia': ["Borrego", "Carens", "Carnival", "Cee'd", "Cerato", "e-Niro", "EV6", "EV9",
    "Magentis", "Mohave", "Niro", "Opirus", "Picanto", "Rio", "Sorento", "Soul",
    "Sportage", "Stinger", "Stonic", "Venga", "XCeed"],
  'Suzuki': ["Alto", "Baleno", "Celerio", "Across", "Grand Vitara", "Ignis", "Jimny",
    "Kizashi", "Liana", "S-Cross", "Splash", "Swift", "SX4", "Vitara", "Wagon R+",
    "XL-7", "Swace"],

  'Abarth': ["124 Spider", "500", "500C", "595", "695", "Grande Punto", "Punto EVO"],
  'Bentley': [ "Arnage", "Azure", "Bentayga", "Continental", "Mulsanne","Flying Spur", "Brooklands"],
  'BYD': ["Atto 3", "Dolphin", "e6", "Han", "Seal", "Seal U", "Tang"],
  'Cadillac': ["ATS", "CT", "CTS", "DeVille", "DTS", "Eldorado", "Escalade", "Seville", "SRX", "STS", "XLR", "XT5", "XT6", "XTS"],
  'Chrysler': ["200", "300C", "300M", "300 SRT", "Crossfire", "Grand Voyager", "Neon", "Pacifica", "PT Cruiser", "Sebring", "Town & Country", "Voyager"],
  'Dacia': ["Dokker","Duster" ,"Jogger" ,"Lodgy" ,"Logan" ,"Pick Up" ,"Sandero" ,"Spring", "Stepway"],
  'Daewoo': ["Espero", "Evanda","Kalos", "Lacetti", "Lanos", "Leganza", "Matiz", "Musso", "Nexia", "Nubira", "Rexton","Tacuma"],
  'Daihatsu': ["Applause", "Charade", "Copen", "Cuore", "Feroza", "Gran Move", "Materia", "Move", "Rocky", "Sirion", "Terios", "Trevis", "YRV"],
  'Dodge': ["Avenger", "Caliber", "Caravan", "Challenger", "Charger", "Dakota", "Dart", "Durango", "Grand Caravan", "Hornet", "Journey", "Magnum", "Neon", "Nitro","RAM", "Viper"],
  'DS': ['DS3', 'DS4', 'DS5'],
  'Honda': ["Accord", "Avancier", "Civic", "CR-V", "CR-Z", "Crosstour", "Clarity", "CRX", "Element", "Fit", "FR-V", "HR-V", "Insight", "Integra", "Jazz", "Legend", "NSX", "Odyssey", "Pilot", "Prelude", "S2000", "Stream", "e", "e:Ny1", "ZR-V"],
  'Hummer': ['H1', 'H2', 'H3', 'HX'],
  'Hyundai': ["Accent", "Azera", "Bayon", "Atos", "Grandeur", "Coupe", "Ioniq", "Creta",
     "Ioniq 5", "Ioniq 6", "Elantra", "Getz", "Genesis", "i10", "i20", "i30",
     "i40", "ix35", "Kona", "Matrix", "Nexo", "Palisade", "Santa Fe", "Sonata",
     "Staria", "Terracan", "Tucson", "Veloster", "Veracruz"],
  'Isuzu': ["Axiom", "Bighorn", "Campo", "D-Max", "Gemini", "Midi", "Rodeo", "Trooper"],
  'Jaguar': ["E-Pace", "E-Type", "F-Type", "F-Pace", "I-Pace", "S-Type", "X-Type", "XE",
    "XF", "XJ", "XK", "XKR"],
  'Jeep': ["Cherokee", "CJ", "Avenger", "Commander", "Compass", "Gladiator",
     "Grand Cherokee", "Liberty", "Patriot", "Renegade", "Wagoneer", "Wrangler"],
  'Lada': ["110", "111", "112", "1200", "2107", "2110", "2111", "2112", "4x4", "Aleko",
     "Granta", "Kalina", "Largus", "Niva", "Nova", "Priora", "Samara", "Vesta",
     "Urban", "X-Ray"],
  'Lancia': ["A112", "Appia", "Beta", "Dedra", "Delta", "Flaminia", "Flavia", "Fulvia",
     "Gamma", "Kappa", "Lybra", "Musa", "Phedra", "Prisma", "Stratos", "Thema",
     "Thesis", "Ypsilon", "Zeta"],
  'Land Rover': ["Defender", "Discovery", "Discovery Sport", "Freelander", "Range Rover",
    "Range Rover Evoque", "Range Rover Sport", "Range Rover Velar"],
  'Lexus': ["CT 200h", "LBX", "LFA", "LM", "ES 300", "ES 330", "ES 350", "GS 200",
     "GS 250", "GS 300", "GS 350", "GS 430", "GS 450", "GS 460", "GX 470",
     "IS 200", "IS 220", "IS 250", "IS 300", "IS 350", "IS-F", "LC 500", "LS 400",
     "LS 430", "LS 460", "LS 500", "LS 600", "LX 470", "LX 570", "NX 200",
     "NX 300", "RC 200", "RC 300", "RC 350", "RC F", "RX 200", "RX 300", "RX 330",
     "RX 350", "RX 400", "RX 450", "RX 500", "SC 400", "SC 430", "UX 200",
     "UX 250", "UX 300", "RZ"],
  'Maserati': ["3200", "4200", "Alfieri", "Bora", "Ghibli", "GranCabrio", "Gransport",
     "Granturismo", "Levante", "Grecale", "MC12", "MC20", "Quattroporte", "Spyder"],
  'Mazda': ["2", "3", "5", "6", "323", "626", "929", "BT-50", "CX-3", "CX-30", "CX-5",
     "CX-60", "CX-7", "CX-9", "CX-80", "Demio", "MX-3", "MX-5", "MX-30", "MPV",
     "Premacy", "RX-7", "RX-8", "Tribute"],
  'Mini': [ "Aceman", "Cabrio", "Clubman", "Clubvan", "Cooper", "Cooper D", "Cooper S",
       "Cooper SD", "Cooper SE", "Countryman", "John Cooper Works", "One", "One D",
       "Paceman", "Roadster"],
  'Mitsubishi': ["3000 GT", "ASX", "Attrage", "Canter", "Carisma", "Colt", "Eclipse",
    "Eclipse Cross", "FTO", "Galant", "Grandis", "i-MiEV", "L200", "L300",
    "L400", "Lancer", "Mirage", "Montero", "Outlander", "Pajero",
    "Pajero Pinin", "Pajero Sport", "Space Star"],
  'Nissan': ["100 NX", "200 SX", "240 SX", "280 ZX", "300 ZX", "350Z", "370Z", "Almera",
    "Altima", "Ariya", "Armada", "Bluebird", "Cube", "e-NV200", "Frontier",
    "GT-R", "Juke", "Leaf", "Maxima", "Micra", "Murano", "Navara", "Note",
    "NP 300", "NV200", "NV300", "NV400", "Pathfinder", "Patrol", "Pixo",
    "Primastar", "Primera", "Pulsar", "Qashqai", "Sentra", "Serena", "Skyline",
    "Sunny", "Terrano", "Tiida", "Titan", "Versa", "X-Trail"],
  'Porsche': ["356", "550", "718 Spyder", "911", "912", "914", "918", "924", "928", "930",
    "944", "959", "962", "968", "991", "992", "993", "996", "997", "964",
    "Boxster", "Carrera GT", "Cayenne", "Cayman", "Macan", "Panamera", "Targa",
    "Taycan"],
  'Smart': [  "#1", "#3", "Crossblade", "ForFour", "ForTwo", "Roadster"],
  'SsangYong': ['Korando', 'Kyron'],
  'Subaru': ["Ascent", "BRZ", "Crosstrek", "Forester", "Impreza", "Justy", "Legacy",
    "Levorg", "Outback", "SVX", "Tribeca", "WRX", "XV"],
  'Tesla': ["Cybertruck", "Model 3", "Model S", "Model X", "Model Y", "Roadster"],
  'Volvo': ["240", "340", "440", "740", "850", "940", "960", "C30", "C40", "C70",
    "S40", "S60", "S70", "S80", "S90", "V40", "V50", "V60", "V70", "V90",
    "XC40", "XC60", "XC70", "XC90", "EX30", "EX40", "EX90", "P1800"],
  'Yugo': ["45", "55", "60", "65", "Skala", "Florida", "Poly"],
  'Zastava': ["101", "128", "750", "850", "Poly"],
}
let godini = ["1980", "1990", "1991", "1992", "1993", "1994", "1995", "1996","1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013","2014","2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]

const transmissions = ['Автоматски', 'Мануелен']
const fuelTypes = ['Бензин', 'Дизел', 'Електрична', 'Хибрид']
const registrationTypes = ['Македонска', 'Странска']

const search = ref('')

const cars = ref([])

const openCarLink = (link) => {
  window.open(link, '_blank')
}

const carsCSV = async () => {
  try {
    const response = await fetch('koli.csv')
    const csvData = await response.text()

    Papa.parse(csvData, {
      header: true,
      complete: (results) => {
        cars.value = results.data.map((item, index) => ({
          id: index + 1,
          brand: item.brand || '',
          model: item.model || '',
          year: parseInt(item.year) || 2020,
          price: parseInt(item.price) || 0,
          transmission: item.transmission || 'Мануелен',
          fuelType: item.fuel_type || 'Дизел',
          image: item.image_link || 'https://via.placeholder.com/300x180?text=No+Image',
          registration: item.registration || 'Македонска',
          mileage: item.mileage_km || 0,
          damaged: item.damaged === 'True',
          link: item.link || ''
        }))
      },
      error: (error) => {
        console.error('Error parsing CSV:', error)
      }
    })
  } catch (error) {
    console.error('Error loading CSV file:', error)
  }
}

const isMobile = ref(false)

window.addEventListener('resize', () => {
  if (window.innerWidth < 768) {
    isMobile.value = true
  } else {
    isMobile.value = false
    showFilters.value = true
  }
})

onMounted(() => {
  carsCSV()
  if (window.innerWidth < 768) {
    isMobile.value = true
  } else {
      showFilters.value = true // Ensure filters are shown on desktop
    }
})

const carsPerPage = 14
const currentPage = ref(1)

const paginatedCars = computed(() => {
  const start = (currentPage.value - 1) * carsPerPage
  const end = start + carsPerPage
  return filteredCars.value.slice(start, end)
})

const totalPages = computed(() => {
  return Math.ceil(filteredCars.value.length / carsPerPage)
})

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}


//computed tuka
const godiniNad = computed(() => {
  if (!filters.value.yearFrom){
    return godini
  }
  return godini.filter(year=>Number(year)>=filters.value.yearFrom)
});

const godiniPod = computed(() => {
  if (!filters.value.yearFrom){
    return godini
  }
  return godini.filter(year=>Number(year)<=filters.value.yearTo)
});

//ova gi dava site opcii spored modelot
const availableModels = computed(() => {
  return filters.value.brand ? models[filters.value.brand] || [] : [];
});

//ova go setira brendot spored shto izbral korisnikot (two way binding)
const filteredModels = computed({
  get() {
    //ne mora .this
    return filters.value.model;
  },
  set(model) {
    filters.value.model = model;
  }
})

const filteredBrands = computed({
  get() {
    return filters.value.brand;
  },
  set(brend) {
    filters.value.brand = brend
    filters.value.model = null;
    this.availableModels = null;
    this.filteredModels = null;
  }
})

const searchAll = computed(() => {
  return cars.value.filter((car) => {
    let Words = search.value.split(" ")
    return Words.every(word =>
      car.brand.toLowerCase().includes(word) || car.model.toLowerCase().includes(word) || car.year.toString().includes(word)
    );
      });
    });

const filteredCars = computed(() => {
  return cars.value.filter((car) => {
    //ako ne e prazen filters.brand -> napravi ja proverkata (DA NE FRLI NULL)
    const Brand = !filters.value.brand || car.brand === filters.value.brand
    const Model = !filters.value.model || car.model === filters.value.model
    const Price =
      car.price >= filters.value.priceRange[0] &&
      car.price <= filters.value.priceRange[1]
    const Year =
      car.year >= filters.value.yearFrom &&
      car.year <= filters.value.yearTo
    const Transmission =
      !filters.value.transmission || car.transmission === filters.value.transmission
    const Fuel =
      !filters.value.fuelType || car.fuelType === filters.value.fuelType
    const Registration =
      !filters.value.registration || car.registration === filters.value.registration

      return (
        Brand &&
        Model &&
        Price &&
        Year &&
        Transmission &&
        Fuel &&
        Registration
      )
    })
})

watch(filteredCars, () => {
  currentPage.value = 1
})

function resetFilters() {
  filters.value = {
    brand: null,
    model: null,
    priceRange: [priceMin, priceMax],
    yearFrom: yearMin,
    yearTo: yearMax,
    transmission: null,
    fuelType: null,
    registration: null,
  }
}

</script>

<style scoped>
.app {
  width: 90%;
  max-height: 95vh;
  margin: 0 auto;
  background: white;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  padding: 30px;
}


.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

#logo {
  font-size: 2rem;
  font-weight: bold;
}

.main-content {
  display: flex;
}

.sidebar {
  width: 300px;
  max-height: calc(100vh - 200px);
  overflow-y: auto;
  background: #f9f9f9;
  border-radius: 15px;
  padding: 15px;
}

.sidebar * {
  max-width: 100%;
  box-sizing: border-box;
}

.price-range {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
  overflow-y: hidden;

}

.collapsible {
  cursor: pointer;
  padding: 10px;
  width: calc(100% - 20px);
  border: none;
  text-align: left;
}

.collapsible:after {
  content: '\02795';
  font-size: 14px;
}

.collapsible.active:after {
  content: '\2796';
}

.content {
  padding-top: 10px;
  overflow: auto;
  display: block;
  transition: all 0.3s ease-out;
}

.content.show {
  max-height: 100%;
}

.car-list {
  flex: 1;
  overflow-y: auto;
  max-height: 70vh;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
}

.car-card {
  background: #fff;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.car-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.car-info {
  padding: 15px;
}

.car-name {
  display: block;
  font-size: 1rem;
  margin-bottom: 5px;
  color: #555;
  cursor:pointer;
  color: blue;
}

.car-price {
  display: block;
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}

.car-details {
  font-size: 0.9rem;
  color: #777;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 40px;
}

.pagination button {
  background-color: #333;
  color: white;
  border: none;
  padding: 8px 16px;
  font-size: 16px;
  cursor: pointer;
}

.pagination button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination span {
  margin: 0 10px;
  font-size: 16px;
}

.pagination button:hover:enabled {
  background-color: #444;
}

@media (max-width: 768px) {
  .main-content {
    flex-direction: column;
  }
  .sidebar {
    width: 100%;
    margin-bottom: 20px;
  }
  .card-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}



</style>
