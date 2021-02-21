<script>
  import { ThemeWrapper, ThemeToggle } from 'svelte-themer'
  import Sidebar from './Sidebar.svelte'
  import themes from './themes.js'
  import App from './Markdown/App.svx'
  import { onMount } from 'svelte';

  let vw, sidebar_width;
  let width, scrollX, scrollY;
  onMount(() => {
    width = sidebar_width = vw/7;
  })
  function toggleSidebar() {
    width = sidebar_width - width;
  }
  function goToElement() {
    console.log(self);
    scrollX = window.scrollX;
    scrollY = window.scrollY;
    document.getElementById("esse-aqui").scrollIntoView({ block: "center", inline: "center" });
  }
  function goBack() {
    window.scrollTo(scrollX, scrollY);
  }
</script>

<svelte:window bind:innerWidth={vw}/>

<ThemeWrapper themes="{themes}">
<Sidebar bind:width={width} />

<div class="topnavbar">
  <div id="main" style="margin-left: {width}px">
    <ThemeToggle id="one" />
    <button on:click={toggleSidebar}>Sidebar</button>
  </div>
</div>
  
<main style="padding: 20px"> 
  <div class="content-container" style="margin-left: {width-8}px; width: calc({sidebar_width - width}px + {vw * (9/7)}px);">
    <div class="one" style="transition: margin-left .5s linear; width: calc({sidebar_width - width}px + {vw * (5.3/7)}px);">
      {#each Array(10) as _, i}
        <p>{i + 1}</p>
      {/each}
      <button on:click={goToElement}>go to word</button>
      <App />

    </div>
    
    <div class="two">
      {#each Array(25) as _, i}
        <p>{i + 1}</p>
      {/each}
      <button on:click={goBack} id="esse-aqui">word</button>
      {#each Array(25) as _, i}
        <p>{i + 1}</p>
      {/each}
    </div>
  </div>
</main>
</ThemeWrapper>

<style>
:global(html) :global(body){
  width: 100%;
  height: 100%;
}	
:global(html) {
  background-color: var(--theme-colors-background, initial);
  color: var(--theme-colors-text, initial);
  scroll-behavior: smooth;
}
:global(body) {
  /* align-items: center; */
  display: flex;
  font-size: var(--theme-font-size);
}
.topnavbar {
    height: 4em;
      width: 100%; /* 0 width - change this with JavaScript */
      position: fixed; /* Stay in place */
      z-index: 1; /* Stay on top */
      top: 0; /* Stay at the top */
      left: 0;
      background-color: #111; /* Black*/
      overflow: hidden; /* Disable horizontal scroll */
      /* padding-top: 60px; Place content 60px from the top */
      /* transition: 0.5s; 0.5 second transition effect to slide in the topnavbar */
  }
.one {
  background-color: rgba(200,0,0,0.5);
}

.two {
  background-color: rgba(100,255,100,0.5);
}

.one, .two {
  flex: 1 auto;
  box-sizing: border-box;
  padding: 20px 20em;
  border: 3px solid yellow;
  justify-content: center;
  align-content: center;
  align-items: center;
  margin: 0 auto;
  text-align: center;
}
.content-container {
  box-sizing: border-box;
  background-color: blueviolet;
  border: 5px solid red;
  margin: 2.5em 0 0 auto;
  display: flex;
  align-items: flex-start;
  color: white;
  justify-content: space-around;
  flex-flow: row wrap;
}

#main {
    transition: margin-left .5s ease;
    height: auto;
    padding: 20px;
    box-sizing: border-box;
}

main {
  display: grid;
  grid-auto-flow: row;
  grid-template-rows: auto max-content;
  grid-template-areas: 'auto';
}

h1 {
  color: var(--theme-colors-text);
  margin: 0;
  text-transform: lowercase;
  font-size: 4rem;
  font-weight: var(--theme-font-weight-lighter);
}

section {
  display: grid;
  grid-auto-flow: row;
  grid-auto-rows: min-content;
  grid-gap: 2rem;
  place-items: center;
  place-content: center;
  padding: var(--theme-padding-large);
  text-align: center;
  /* max-width: 240px; */
}

#intro {
  grid-area: intro;
}
</style>