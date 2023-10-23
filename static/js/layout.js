document.body.style.overflowY = 'hidden'

document.getElementById('sidebarResponsiveTooglerButton').addEventListener('click', (ev) => {
    const sideBar = document.getElementById('sidebar-container')
    if(sideBar.style.width == '280px'){
        sideBar.style.width = '0px'
        sideBar.style.overflowX = 'hidden'
        sideBar.style.opacity = '0'
    }
    else{
        sideBar.style.width = '280px'
        sideBar.style.overflowX = 'auto'
        sideBar.style.opacity = '1'
    }
})