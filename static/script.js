document.getElementById('searchButton').addEventListener('click', function() {
    // Recupera o valor do input de pesquisa
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    
    // Define o ID da seção correspondente
    let sectionId = '';

    // Verifica qual seção corresponde ao input de pesquisa
    switch (searchInput) {
        case 'camisetas':
            sectionId = 'camisetas';
            break;
        case 'shorts':
            sectionId = 'shorts';
            break;
        case 'calçados':
            sectionId = 'calçados';
            break;
        case 'perfume':
            sectionId = 'perfume';
            break;
        case 'lupas':
            sectionId = 'lupas';
            break;
        case 'conjuntos':
            sectionId = 'conjuntos';
            break;
        case 'tracksuit':
            sectionId = 'tracksuit';
            break;
        case 'promoção':
            sectionId = 'promoção';
            break;
        default:
            alert('Produto não encontrado!');
            return;
    }

    // Rola até a seção correspondente
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
});