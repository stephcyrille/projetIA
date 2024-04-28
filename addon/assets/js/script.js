document.addEventListener('DOMContentLoaded', function() {
  // Réccupération de l'URL lorsqu'on ouvre l'AddOn
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var currentUrl = tabs[0].url;
    var currentTitle = tabs[0].title;
    document.getElementById('url').value = currentUrl;
    document.getElementById('titre').value = currentTitle;

    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      args: [currentUrl],
      func: setContentAndAuthor
    });
  });

  openTab('prediction');
  document.getElementById('result').style.display = 'none';
  // Gestionnaire d'événement pour le formulaire de prédiction
  document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Pour empêcher le formulaire de se soumettre normalement

    // Afficher le bloc de chargement
    document.getElementById('loading-overlay').style.display = 'flex';

    // Cacher le contenu de la page
    document.getElementById('prediction').style.display = 'none';
    document.getElementById('predictions-passees').style.display = 'none';

    // Attendre pendant 5 secondes
    setTimeout(function() {
        // Cacher le bloc de chargement
        document.getElementById('loading-overlay').style.display = 'none';

        // Afficher la page de résultat
        const resultsList = ["real", "fake"];
        const random = Math.floor(Math.random() * resultsList.length);
        toggleBlockResult('result', random);
    }, 4000);
  });

  // Gestionnaires d'événements pour les onglets
  document.getElementById('prediction-tab').addEventListener('click', function() {
      openTab('prediction');
  });

  document.getElementById('predictions-passees-tab').addEventListener('click', function() {
      openTab('predictions-passees');
  });
  
  document.getElementById('closeItemIcon').addEventListener('click', function() {
    handleCloseResultCard();
  });
  
  document.getElementById('backToHome').addEventListener('click', function() {
    handleBackToHome('result');
  });
});

// Fonction pour ouvrir un onglet
function openTab(tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName('tabcontent');
  tablinks = document.getElementsByClassName('tablinks');
  for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = 'none';
      tablinks[i].classList.remove('active');
  }
  document.getElementById(tabName).style.display = 'block';
  document.getElementById(tabName + '-tab').classList.add('active');
}

// Fonction pour ouvrir le bloc succès
function toggleBlockResult(blockName, result) {
  document.getElementById(blockName).style.display = 'block';

  if(result === 1){
    document.getElementById('resultImg').src = './assets/img/failed.png'
    document.getElementById('resultImg').alt = 'Thumb down'
    document.getElementById('resultTitle').innerText = "Fake news"
    document.getElementById('resultMsg').innerText = "Donner les raisons pour laquelle l'information est fausse et dire l'information pluto vraie"
  } else {
    document.getElementById('resultImg').src = './assets/img/success.png'
    document.getElementById('resultImg').alt = 'Thumb up'
    document.getElementById('resultTitle').innerText = "Information vraie"
    document.getElementById('resultMsg').innerText = "Un petit commentaire au sujet de l'information ou de la source"
  }
  

  // Cachons les autres blocks
  document.getElementById('tab_nav').style.display = 'none';
  document.getElementById('prediction').style.display = 'none';
  document.getElementById('predictions-passees').style.display = 'none';
}


// Fonction pour fermer la carte de succès
function handleCloseResultCard() {
  window.close()
}

// Fonction pour fermer la carte de succès
function handleBackToHome(blockName) {
  document.getElementById(blockName).style.display = 'none';

  // Ouvrons les autres blocks
  document.getElementById('tab_nav').style.display = 'block';
  openTab('prediction');
}

function setContentAndAuthor(url) {
  function extractMetaTags(metaName) {
    const metas = document.getElementsByTagName('meta');
    
    for (let i = 0; i < metas.length; i++) {
      if (metas[i].getAttribute('name') === metaName) {
        return metas[i].getAttribute('content');
      }
    }
    
    return '';
  }

  // Send extracted meta tags to the extension's background script
  let description = extractMetaTags('description');
  let author = extractMetaTags('author');
  let baseURL = url.replace(/^https:\/\/www\./i, '').replace(/\.com\/.*$/, '');
  // Capitalize the base URL
  baseURL = baseURL.charAt(0).toUpperCase() + baseURL.slice(1);

  chrome.runtime.sendMessage({ 
      action: 'getMetas', 
      metaTags: {
        author: author, 
        description: description,
        alternativeAuthor: baseURL
      } 
  });
}

chrome.runtime.onMessage.addListener((message) => {
  console.log(message)
  if (message.action === 'getMetas') {
    document.getElementById('contenu').value = message.metaTags.description;
    document.getElementById('auteur').value = message.metaTags.author;

    if(message.metaTags.author === ''){
      document.getElementById('auteur').value = message.metaTags.alternativeAuthor;
    }
  }
});