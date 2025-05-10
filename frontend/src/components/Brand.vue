<template>
<div class="page">
  <h1 id="logo">KupiVozi</h1>
  <span class="back" @click="navigateTo('/price')">←</span>

  <ProgressBar :value="progress"></ProgressBar>

  <div class="w3-light-grey">
    <div style="width:75%; background-color:#8058ee"></div>
  </div>

  <h1 id="tagline">Кој ви се омилените брендови?</h1>

  <h4>DEBUG: {{checkedNames}}</h4>
  <div id="all">
    <h4 id="allText">Сите</h4>
  </div>

  <div class="brands">
    <h2 class="letter">A</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(2)', 'abarth')">
        <img :src="abarth">
        <h4 class="selection">Abarth</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(3)', 'alfaromeo')">
        <img :src="alfaromeo">
        <h4 class="selection">Alfa Romeo</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(4)', 'aston')">
        <img :src="aston">
        <h4 class="selection">Aston Martin</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(5)', 'audi')">
        <img :src="audi">
        <h4 class="selection">Audi</h4>
    </div>

    <h2 class="letter">B</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(7)', 'bentley')">
        <img :src="bentley">
        <h4 class="selection">Bentley</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(8)', 'bmw')">
        <img :src="bmw">
        <h4 class="selection">BMW</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(9)', 'byd')">
        <img :src="byd">
        <h4 class="selection">BYD</h4>
    </div>

    <h2 class="letter">C</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(11)', 'cadillac')">
        <img :src="cadillac">
        <h4 class="selection">Cadillac</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(12)', 'chevrolet')">
        <img :src="chevrolet">
        <h4 class="selection">Chevrolet</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(13)', 'chrysler')">
        <img :src="chrysler">
        <h4 class="selection">Chrysler</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(14)', 'citroen')">
        <img :src="citroen">
        <h4 class="selection">Citroen</h4>
    </div>

    <h2 class="letter">D</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(16)', 'dacia')">
        <img :src="dacia">
        <h4 class="selection">Dacia</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(17)', 'daewoo')">
        <img :src="daewoo">
        <h4 class="selection">Daewoo</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(18)', 'daihatsu')">
        <img :src="daihatsu">
        <h4 class="selection">Daihatsu</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(19)', 'dodge')">
        <img :src="dodge">
        <h4 class="selection">Dodge</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(20)', 'ds')">
        <img :src="ds">
        <h4 class="selection">DS Automobiles</h4>
    </div>

    <h2 class="letter">F</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(22)', 'ferrari')">
        <img :src="ferrari">
        <h4 class="selection">Ferrari</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(23)', 'fiat')">
        <img :src="fiat">
        <h4 class="selection">Fiat</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(24)', 'ford')">
        <img :src="ford">
        <h4 class="selection">Ford</h4>
    </div>

    <h2 class="letter">G</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(26)', 'gmc')">
        <img :src="gmc">
        <h4 class="selection">GMC</h4>
    </div>

    <h2 class="letter">H</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(28)', 'honda')">
        <img :src="honda">
        <h4 class="selection">Honda</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(29)', 'hyundai')">
        <img :src="hyundai">
        <h4 class="selection">Hyundai</h4>
    </div>

    <h2 class="letter">J</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(31)', 'jaguar')">
        <img :src="jaguar">
        <h4 class="selection">Jaguar</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(32)', 'jeep')">
        <img :src="jeep">
        <h4 class="selection">Jeep</h4>
    </div>

    <h2 class="letter">K</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(34)', 'kia')">
        <img :src="kia">
        <h4 class="selection">Kia</h4>
    </div>

    <h2 class="letter">L</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(36)', 'lamborghini')">
        <img :src="lamborghini">
        <h4 class="selection">Lamborghini</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(37)', 'landrover')">
        <img :src="landrover">
        <h4 class="selection">Land Rover</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(38)', 'lexus')">
        <img :src="lexus">
        <h4 class="selection">Lexus</h4>
    </div>

    <h2 class="letter">M</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(40)', 'maserati')">
        <img :src="maserati">
        <h4 class="selection">Maserati</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(41)', 'mazda')">
        <img :src="mazda">
        <h4 class="selection">Mazda</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(42)', 'mercedes')">
        <img :src="mercedes">
        <h4 class="selection">Mercedes-Benz</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(43)', 'mini')">
        <img :src="mini">
        <h4 class="selection">Mini</h4>
    </div>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(44)', 'mitsubishi')">
        <img :src="mitsubishi">
        <h4 class="selection">Mitsubishi</h4>
    </div>

    <h2 class="letter">N</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(46)', 'nissan')">
        <img :src="nissan">
        <h4 class="selection">Nissan</h4>
    </div>

    <h2 class="letter">O</h2>
    <div class="cmbn" @click="changeColor('.cmbn:nth-child(48)', 'opel')">
        <img :src="opel">
        <h4 class='selection'>Opel</h4>
    </div>

    <h2 class='letter'>P</h2>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(50)", "peugeot")'>
        <img :src='peugeot'>
        <h4 class='selection'>Peugeot</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(51)", "pontiac")'>
        <img :src='pontiac'>
        <h4 class='selection'>Pontiac</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(52)", "porsche")'>
        <img :src='porsche'>
        <h4 class='selection'>Porsche</h4>
    </div>

    <h2 class='letter'>R</h2>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(54)", "renault")'>
        <img :src='renault'>
        <h4 class='selection'>Renault</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(55)", "rollsroyce")'>
        <img :src='rr'>
        <h4 class='selection'>Rolls-Royce</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(56)", "rover")'>
        <img :src='rover'>
        <h4 class='selection'>Rover</h4>
    </div>

    <h2 class='letter'>S</h2>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(58)", "saab")'>
        <img :src='saab'>
        <h4 class='selection'>Saab</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(59)", "seat")'>
        <img :src='seat'>
        <h4 class='selection'>Seat</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(60)", "skoda")'>
        <img :src='skoda'>
        <h4 class='selection'>Skoda</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(61)", "smart")'>
        <img :src='smart'>
        <h4 class='selection'>Smart</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(62)", "ssangyong")'>
        <img :src='ssangyong'>
        <h4 class='selection'>Ssangyong</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(63)", "subaru")'>
        <img :src='subaru'>
        <h4 class='selection'>Subaru</h4>
    </div>
    <div class='cmbn' @click='changeColor(".cmbn:nth-child(64)", "suzuki")'>
        <img :src='suzuki'>
        <h4 class='selection'>Suzuki</h4>
    </div>

    <h2 class="letter">T</h2>
    <div class="cmbn" @click='changeColor(".cmbn:nth-child(66)", "tesla")'>
        <img :src="tesla">
        <h4 class="selection">Tesla</h4>
    </div>
    <div class="cmbn" @click='changeColor(".cmbn:nth-child(67)", "toyota")'>
        <img :src="toyota">
        <h4 class="selection">Toyota</h4>
    </div>

    <h2 class="letter">V</h2>
    <div class="cmbn" @click='changeColor(".cmbn:nth-child(69)", "vw")'>
        <img :src="vw">
        <h4 class="selection">VW Volkswagen</h4>
    </div>
    <div class="cmbn" @click='changeColor(".cmbn:nth-child(70)", "volvo")'>
        <img :src="volvo">
        <h4 class="selection">Volvo</h4>
    </div>

    <h2 class="letter">YZ</h2>
    <div class="cmbn" @click='changeColor(".cmbn:nth-child(72)", "yugo")'>
        <img :src="yugo">
        <h4 class="selection">Yugo</h4>
    </div>
    <div class="cmbn" @click='changeColor(".cmbn:nth-child(73)", "zastava")'>
        <img :src="zastava">
        <h4 class="selection">Zastava</h4>
    </div>
  </div>

 <br><br><br><br><br><br>
 <Button label="Следно" severity="success" variant="text" raised @click="navigateTo('/engine')"/>
 </div>
</template>

<script>

import abarth from '@/assets/brands/abarth.png'; import alfaromeo from '@/assets/brands/alfaromeo.png'; import aston from '@/assets/brands/aston.png'; import audi from '@/assets/brands/audi.png'; import bentley from '@/assets/brands/bentley.png';
import bmw from '@/assets/brands/bmw.png'; import byd from '@/assets/brands/byd.png'; import cadillac from '@/assets/brands/cadillac.png'; import chevrolet from '@/assets/brands/chevrolet.png'; import chrysler from '@/assets/brands/chrysler.png';
import citroen from '@/assets/brands/citroen.png'; import dacia from '@/assets/brands/dacia.png'; import daewoo from '@/assets/brands/daewoo.png'; import daihatsu from '@/assets/brands/daihatsu.png';
import dodge from '@/assets/brands/dodge.png'; import ds from '@/assets/brands/ds.png'; import ferrari from '@/assets/brands/ferrari.png'; import fiat from '@/assets/brands/fiat.png';
import ford from '@/assets/brands/ford.png'; import gmc from '@/assets/brands/gmc.png'; import honda from '@/assets/brands/honda.png'; import hummer from '@/assets/brands/hummer.png'; import hyundai from '@/assets/brands/hyundai.png';
 import infinity from '@/assets/brands/infinity.png'; import isuzu from '@/assets/brands/isuzu.png'; import jaguar from '@/assets/brands/jaguar.png'; import jeep from '@/assets/brands/jeep.png';
import kia from '@/assets/brands/kia.png'; import lada from '@/assets/brands/lada.jpg'; import lamborghini from '@/assets/brands/lamborghini.png'; import lancia from '@/assets/brands/lancia.png';
import landrover from '@/assets/brands/landrover.png'; import lexus from '@/assets/brands/lexus.png'; import lotus from '@/assets/brands/lotus.png'; import maserati from '@/assets/brands/maserati.png';
import maybach from '@/assets/brands/maybach.png'; import mazda from '@/assets/brands/mazda.png'; import mercedes from '@/assets/brands/mercedes.png'; import mg from '@/assets/brands/mg.png';
import mini from '@/assets/brands/mini.png'; import mitsubishi from '@/assets/brands/mitsubishi.png'; import nissan from '@/assets/brands/nissan.png'; import opel from '@/assets/brands/opel.png';
import peugeot from '@/assets/brands/peugeot.png'; import pontiac from '@/assets/brands/pontiac.png'; import porsche from '@/assets/brands/porsche.png'; import renault from '@/assets/brands/renault.png';
import rover from '@/assets/brands/rover.png'; import rr from '@/assets/brands/rr.png'; import saab from '@/assets/brands/saab.png'; import seat from '@/assets/brands/seat.png'; import skoda from '@/assets/brands/skoda.png';
import smart from '@/assets/brands/smart.png'; import ssangyong from '@/assets/brands/ssangyong.png'; import subaru from '@/assets/brands/subaru.png'; import suzuki from '@/assets/brands/suzuki.png'; import tesla from '@/assets/brands/tesla-logo-2007-full-download.png';
import toyota from '@/assets/brands/toyota-logo-2020-europe-download.png'; import volvo from '@/assets/brands/volvo.png'; import vw from '@/assets/brands/vw.png'; import yugo from '@/assets/brands/yugo.png'; import zastava from '@/assets/brands/zastava.jpg';

export default {
  components: {
  },
  name: 'BrandPage',
  data() {
    return {
      progress: 40,
      abarth, alfaromeo, aston, audi, bentley, bmw, byd, cadillac, chevrolet, chrysler, citroen, dacia, daewoo, daihatsu, dodge, ds, ferrari, fiat, ford, gmc, honda, hummer, hyundai, infinity, isuzu, jaguar, jeep, kia, lada, lamborghini, lancia, landrover, lexus, lotus, maserati, maybach, mazda, mercedes, mg, mini, mitsubishi, nissan, opel, peugeot, pontiac, porsche, renault, rover, rr, saab, seat, skoda, smart, ssangyong, subaru, suzuki, tesla, toyota, volvo, vw, yugo, zastava,
      checkedNames: (["all"]),
      isActive: false,
    };
  },
  methods: {
    navigateTo(x) {
      //smeni strana
      this.$router.push({ path: `${x}` })
    },
    changeColor(el, name) {
      let toj = document.querySelector(el)
      if (toj) {
        document.getElementById("all").style.backgroundColor = 'transparent'
        document.getElementById("allText").style.color = 'black'
        this.checkedNames = this.checkedNames.filter(item => item !== "all")
        let tekst = toj.children
        if (toj.style.backgroundColor == "transparent") {
          this.checkedNames.push(name)
          toj.style.backgroundColor = '#8058ee'
          tekst[1].style.color = 'white'
        }
        else {
          //proverka na sekoj item od array
          this.checkedNames = this.checkedNames.filter(item => item !== name)
          toj.style.backgroundColor = "transparent"
          tekst[1].style.color = 'black'
          if (this.checkedNames.length == 0){
            this.checkedNames.push("all")
            document.getElementById("all").style.backgroundColor = '#8058ee'
            document.getElementById("allText").style.color = 'white'
            console.log("all")
          }
        }
      }
      else{
        console.log("cant find element")
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
  .letter {
      display:flex;
  }

  .selection{
      outline: solid;
      outline-width: 0.5px;
      border-radius: 5px;
      height: 2.5em;
      display: flex;
      align-items: center;
      justify-content: left;
      padding-left: 3.25em;
  }
  .cmbn{
      margin:0;
      padding: 0;
      margin-top: -2em;
      display: grid;
      cursor: pointer;
      user-select: none;
  }
  .cmbn img{
      width: 3.15em;
      height: 3.15em;
      object-fit:scale-down;
      padding-top: 1.5em;
      margin-top: 0.28em;
      margin-bottom: -10em;
      -webkit-user-drag: none;
      -moz-window-dragging:no-drag;
  }
  #all{
      outline: solid;
      outline-width: 0.5px;
      border-radius: 5px;
      height: 2.5em;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background-color: #8058ee
  }
  #all h4{
      color:white;
  }
</style>
