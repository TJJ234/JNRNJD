<template>
<div class="page">
  <h1 id="logo">KupiVozi</h1>
  <span class="back" @click="navigateTo('/engine')">←</span>

  <ProgressBar :value="progress"></ProgressBar>

  <div class="w3-light-grey">
    <div style="width:75%; background-color:#8058ee"></div>
  </div>

  <h1 id="tagline">Што преферирате?</h1>
  <br />

  <div class="image-selection">
      <div v-for="image in images" :key="image.id" class="image-item" @click="toggleSelection(image.id)">
        <img :src="image.src" :alt="image.alt">
        <div class="checkmark" v-show="image.selected">✓</div>
        <h4>{{image.text}}</h4>
      </div>
  </div>

 <br><br><br><br><br><br>
 <Button label="Следно" severity="success" variant="text" raised @click="navigateTo('/type')"/>
</div>
</template>

<script>
import manuel from '@/assets/transmission/manuel.png'
import automatic from '@/assets/transmission/automatic.png'


export default {
  components: {
  },
  name: 'TransmissionSelection',
  data() {
    return {
      progress: 80,
      images: [
        { id: 1, src: manuel, alt: 'Benzin', selected: true, text:"Мануелен менувач"},
        { id: 2, src: automatic, alt: 'Diesel', selected: true, text:"Автоматски менувач"},
            ]
    };
  },
  methods: {
    navigateTo(x) {
      //smeni strana
      this.$router.push({ path: `${x}` })
    },
    toggleSelection(id) {
          const image = this.images.find(img => img.id === id);
          if (image) {
            image.selected = !image.selected;
          }
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
  .image-selection {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }

    .image-item {
      position: relative;
      cursor: pointer;
      width: 300px;
      height: 150px;
      overflow: hidden;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .image-item img {
      height: 65%;
      user-drag: none;
      -webkit-user-drag: none;
      user-select: none;
      -moz-user-select: none;
      -webkit-user-select: none;
      -ms-user-select: none;
    }

    .checkmark {
      position: absolute;
      top: 10px;
      right: 10px;
      background-color: #8058ee;
      color: white;
      border-radius: 50%;
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
    }
</style>
