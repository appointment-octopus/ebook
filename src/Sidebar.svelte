<script>
    export let width;
</script>

<div id="mySidenav" class="sidenav" style="width: {width}px"> 
    <a href="#">About</a>
    <a href="#">Services</a>
    <a href="#">Clients</a>
    <a href="#">Contact</a>
</div>

<style>
    /* The side navigation menu */
    .sidenav {
        height: 100%; /* 100% Full-height */
        width: 0; /* 0 width - change this with JavaScript */
        position: fixed; /* Stay in place */
        z-index: 1; /* Stay on top */
        top: 0; /* Stay at the top */
        left: 0;
        background-color: #111; /* Black*/
        overflow-x: hidden; /* Disable horizontal scroll */
        padding-top: 60px; /* Place content 60px from the top */
        transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
    }
    
    /* The navigation menu links */
    .sidenav a {
        padding: 8px 8px 8px 32px;
        text-decoration: none;
        font-size: 25px;
        color: #818181;
        display: block;
        transition: 0.5s;
    }
    
    /* When you mouse over the navigation links, change their color */
    .sidenav a:hover {
        color: #f1f1f1;
    }
    
    /* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
    @media screen and (max-height: 450px) {
        .sidenav {padding-top: 15px;}
        .sidenav a {font-size: 18px;}
    }
</style>
