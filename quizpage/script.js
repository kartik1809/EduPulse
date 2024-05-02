const div = document.querySelector('.home-container')
fetch('nav.html')
.then(res=>res.text())
.then(data=>{
    div.innerHTML=data
    const parser = new DOMParser()
    const doc = parser.parseFromString(data, 'text/html')
    eval(doc.querySelector('script').textContent)
})