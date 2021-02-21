<script>
  import { ThemeWrapper, ThemeToggle } from 'svelte-themer'
  import Sidebar from './Sidebar.svelte'
  import themes from './themes.js'
  import App from './Markdown/App.svx'
  import { onMount } from 'svelte';

  let vw;
  let show = true, scrollX, scrollY;

  function toggleSidebar() {
    show = !show;
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
<div class="{show ? 'grid-container' : 'grid-no-sidebar' }" >
  {#if show === true}
    <div class="sidebar">
      <ul>
        {#each Array(75) as _, i}
        <li>{i + 1}</li>
      {/each}      </ul>
    </div>
  {/if}

  <div class="topbar">
    <div class="icons">
      <div class="theme">
        <ThemeToggle id="one" />
      </div>
      <div class="sidebar-toggle">
        <button on:click={toggleSidebar}>Sidebar</button>
      </div>
    </div>
  </div>


    <div class="one" style="width: {show ? 85 : 100}vw;"></div>
    <div class="two"></div>
</div>
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
  align-items: center;
  display: flex;
  font-size: var(--theme-font-size);
}

.grid-container {
  /* width: 100%; */
  margin: 0 auto;
  height: 100%;
  display: grid;
  grid-template-columns: repeat(8, auto);
  grid-template-rows: 1fr 32fr;
  gap: 0px 0px;
  grid-template-areas:
    "sidebar topbar topbar topbar topbar topbar topbar two"
    "sidebar one one one one one one two";
}

.grid-no-sidebar {
  /* width: 100%; */
  height: 100%;
  display: grid;
  grid-template-columns: repeat(8, auto);
  grid-template-rows: 1fr 32fr;
  gap: 0px 0px;
  grid-template-areas:
    "topbar topbar topbar topbar topbar topbar topbar two"
    "one one one one one one one two";
}

.sidebar { 
  position: fixed;
  left: 0;
  top: 0;
  overflow: hidden;
  background-color: pink;
  grid-area: sidebar;
  width: 15vw;
}

.topbar {
  position: sticky;
  left: 0;
  top: 0;
  margin: 0;
  width: calc(100% - 1vw);
  box-sizing: border-box;
  display: grid;
  background-color: blue;
  grid-template-columns: repeat(9, 1fr);
  grid-template-rows: 1fr;
  grid-template-areas: "icons . . . . . . .";
  grid-area: topbar;
}

.icons {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 1fr;
  gap: 0px 0px;
  grid-template-areas: "sidebar-toggle theme";
  grid-area: icons;
  background-color: black;
}

.theme { background-color: red; grid-area: theme; }
.sidebar-toggle { grid-area: sidebar-toggle; background-color: cyan;}

.one { grid-area: one; left:0; background-color: rgba(200,200,200,0.5)}

.two { grid-area: two; background-color: purple; width: 40vw;}

</style>