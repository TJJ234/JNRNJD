<template>
<div class="page">
  <h1 id="logo">KupiVozi</h1>
  <span class="back" @click="navigateTo('/transmission')">←</span>

  <ProgressBar :value="progress"></ProgressBar>

  <div class="w3-light-grey">
    <div style="width:75%; background-color:#8058ee"></div>
  </div>

  <h1 id="tagline">Каков тип на возило сакате?</h1>
  <br />

  <div class="image-selection">
      <div v-for="image in images" :key="image.id" class="image-item" @click="toggleSelection(image.id)">
        <img :src="image.src" :alt="image.alt">
        <div class="checkmark" v-show="image.selected">✓</div>
      </div>
    </div>

 <br><br><br><br><br><br>
 <Button label="Следно" severity="success" variant="text" raised @click="navigateTo('/brand')"/>
</div>
</template>

<script>

import cabrio from '@/assets/types/cabriolet.png'
import caravan from '@/assets/types/caravan.png'
import coupes from '@/assets/types/coupes.png'
import hatchback from '@/assets/types/hatchback.png'
import sedan from '@/assets/types/sedan.png'
import suv from '@/assets/types/suv.png'

export default {
  components: {
  },
  name: 'TypePage',
  data() {
    return {
      progress: 99,
      images: [
        { id: 1, src: sedan, alt: 'Sedan', selected: true },
        { id: 2, src: hatchback, alt: 'Hatchback', selected: true },
        { id: 3, src: suv, alt: 'Suv', selected: true },
        { id: 4, src: coupes, alt: 'Coupes', selected: true },
        { id: 5, src: caravan, alt: 'Caravan', selected: true },
        { id: 6, src: cabrio, alt: 'Cabrio', selected: true },
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
      width: 75%;
      height: 75%;
      object-fit: cover;
      user-drag: none;
      -webkit-user-drag: none;
      user-select: none;
      -moz-user-select: none;
      -webkit-user-select: none;
      -ms-user-select: none;
    }

    .image-item:nth-child(1) img {
      width: 100%;
      height: 81%;
      object-fit: cover;
      padding-bottom: 5px;
    }

    .image-item:nth-child(2) img {
      object-fit: cover;
      padding-top: 6px;
    }

    .image-item:nth-child(3) img {
      object-fit: cover;
      padding-top: 15px;
    }

    .image-item:nth-child(4) img {
      object-fit: cover;
      padding-top: 5px;
    }

    .image-item:nth-child(5) img {
      object-fit: cover;
      padding-top: 5px;
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
