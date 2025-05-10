<template>
  <div class="page">
    <h1 id="logo">KupiVozi</h1>
    <span class="back" @click="navigateTo('/')">←</span>

    <ProgressBar :value="progress"></ProgressBar>

    <div class="w3-light-grey">
      <div class="w3-blue" style="width:75%"></div>
    </div>

    <h1 id="tagline">Колкав е вашиот буџет?</h1>
    <br />

   <h1 v-if="number1!=0 || number2!=30000" >{{ number1 }} - {{ number2 }}</h1>
   <h1 v-else>Било која цена</h1>
   <Slider v-model="value" range :min=0 :max=30000 :step=500 class="w-56" @update:model-value="separateSlider()" />

   <br><br><br><br><br><br>
   <Button label="Следно" severity="success" variant="text" raised @click="navigateTo('/brand')"/>
  </div>
</template>


  <script>
  import Slider from 'primevue/slider';

  export default {
    components: {
      Slider,
    },
    name: 'PricePage',
    data() {
      return {
        showPopup: false,
        items: [
          "Пример 1",
          "Пример 2",
          "Пример 3",
          "Пример 4",
          "Пример 5",
          "Пример 6",
          "Пример 7",
          "Пример 8",
          "Пример 9",
          "Пример 10",
        ],
        value: 0,
        number1: 0,
        number2: 30000,
        progress: 20,
      };
    },
    props: {
      msg: String
    },
    methods: {
      navigateTo(x) {
        //smeni strana
        this.$router.push({ path: `${x}` })
      },
      togglePopup() {
        //za menito
        this.showPopup = !this.showPopup;
      },
      separateSlider() {
        [this.number1, this.number2] = this.value
      }
    }
  }
  </script>

  <style scoped>
    .page {
      margin-left: 20%;
      margin-right: 40%;
    }
    #logo {
      font-size: x-large;
    }
    #tagline {
      font-size: 1.75em;
      font-weight: bold;
    }
    span {
      display:flex;
      justify-content: left;
      align-items: center;
    }
    h1 {
      display:flex;
      justify-content: left;
      align-items: center;
    }
    h3 {
      display:flex;
      justify-content: left;
      align-items: center;
      text-decoration: underline;
    }
    .back {
      color: #6325e6;
      cursor: pointer;
    }
  </style>
