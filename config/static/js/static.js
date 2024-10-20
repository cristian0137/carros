document.addEventListener('DOMContentLoaded',()=>{
    const form = document.getElementById('libro-form')
    const mensaje = document.getElementById('mensaje')

    form.addEventListener('submit',(e)=>{
        e.preventDefault()

        const modelo = document.getElementById('modelo').value;
        const color = document.getElementById('color').value;
        const puertas = parseInt(document.getElementById('puertas').value)

        carro={modelo,color,puertas}
        
        fetch('Agregarcarro',{
            method:'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body : JSON.stringify(carro)
        })
        .then(response =>{
            if(response.status===200){
                mensaje.textContent = 'Carro agregado'
                mensaje.style.color = 'blue'
                form.reset()
            }
        })
        .catch(() =>{
            mensaje.textContent = 'Error al agregar el libro.';
            mensaje.style.color = 'blue';
        })
    })
})