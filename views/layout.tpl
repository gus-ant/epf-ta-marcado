<!DOCTYPE html>
<html lang="pt-br">

<!-- No Layout eu coloquei o CSS embutido pois não consegui colocar ele no Style.css para funcionar realmente -->
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tá Marcado – {{title or 'Sistema'}}</title>

  <!-- Fonte -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet" />

  <!-- CSS embutido -->
  <style>
    :root {
      --primary-color: #5d5df5;
      --primary-color-hover: #4b4bf0;
      --secondary-color: #2b2d55;
      --success-color: #2ecc71;
      --danger-color: #e74c3c;
      --text-color: #25314b;
      --muted-text-color: #7f8c8d;
      --light-gray: #f5f7fa;
      --border-color: #e0e0e0;
      --radius: 12px;
      --shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
      --transition: all 0.25s ease;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Poppins', sans-serif;
      font-size: 16px;
      line-height: 1.6;
      background: var(--light-gray);
      color: var(--text-color);
      -webkit-font-smoothing: antialiased;
    }

    a {
      text-decoration: none;
      color: var(--primary-color);
      transition: var(--transition);
    }

    a:hover {
      color: var(--primary-color-hover);
    }

    .container {
      width: 100%;
      max-width: 1200px;
      padding: 0 20px;
      margin: 0 auto;
    
    }

    /* NAVBAR */
    .navbar {
      background: #fff;
      border-bottom: 1px solid #eee;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 4px rgba(0, 0, 0, .03);
      
    }

    .navbar .container {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 1rem 0;
    }

    .navbar-brand {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--primary-color);
    }

    .navbar-nav {
      display: flex;
      gap: 1.4rem;
      list-style: none;
    }

    .nav-link {
      font-size: 1rem;
      color: var(--text-color);
      padding: .4rem .2rem;
      border-radius: 4px;
      transition: var(--transition);
    }

    .nav-link:hover {
      color: var(--primary-color);
      background: var(--light-gray);
    }

    .navbar-toggler {
      display: none;
      font-size: 1.5rem;
      background: none;
      border: none;
      cursor: pointer;
    }

    .collapse {
      display: flex;
    }

    @media (max-width: 768px) {
      .navbar-toggler {
        display: block;
      }

      .collapse {
        display: none;
        flex-direction: column;
        align-items: flex-start;
        padding-top: 1rem;
      }

      .collapse.show {
        display: flex;
      }
    }


    /* ----- GRID DE EVENTOS 3× POR LINHA ----- */
.events-grid{
  display: grid;
  gap: 24px;
  /* Padrão desktop – exatamente 3 colunas */
  grid-template-columns: repeat(3, 1fr);
}

/* Tablets: 2 colunas */
@media (max-width: 991px){
  .events-grid{
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Mobile: 1 coluna */
@media (max-width: 576px){
  .events-grid{
    grid-template-columns: 1fr;
  }
}


    footer {
      padding: 40px 0;
      text-align: center;
      color: var(--muted-text-color);
      font-size: 0.9rem;
    }

    /* Utilitário botão padrão */
    .btn {
      padding: 10px 20px;
      background: var(--primary-color);
      color: #fff;
      font-weight: 600;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: var(--transition);
      display: inline-block;
      text-align: center;
    }

    .btn:hover {
      background: var(--primary-color-hover);
    }

    .card img {
  width: 250px;
  height: 200px;          
  object-fit: cover;      
  border-top-left-radius: var(--radius);
  border-top-right-radius: var(--radius);
}

.table-container {
  overflow-x: auto;
  background: #fff;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

.styled-table thead {
  background: var(--primary-color);
  color: white;
  text-align: left;
}

.styled-table th, .styled-table td {
  padding: 14px 18px;
  border-bottom: 1px solid var(--border-color);
}

.styled-table tr:hover {
  background-color: var(--light-gray);
}

.styled-table a {
  color: var(--primary-color);
  font-weight: 500;
}

.actions {
  display: flex;
  gap: 8px;
  align-items: center;
}

.btn-sm {
  font-size: 0.85rem;
  padding: 6px 10px;
  border-radius: 6px;
}

.btn-edit {
  background-color: #f1c40f;
  color: #fff;
}

.btn-edit:hover {
  background-color: #d4ac0d;
}

.btn-danger {
  background-color: var(--danger-color);
  color: #fff;
  border: none;
  cursor: pointer;
  transition: var(--transition);
}

.btn-danger:hover {
  background-color: #c0392b;
}

// .hero-banner {
//   background: url('/static/img/banner.png') center center / cover no-repeat;

//   padding: 60px 20px;
//   color: white;
//   text-align: center;
// }

.hero-banner {
  background: url('/static/img/banner.png') center center / cover no-repeat;
  padding: 80px 20px;
  color: white;
  text-align: center;
  position: relative;
}

.hero-banner::before {
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45); /* escurece o fundo */
  z-index: 0;
  border-radius: inherit;
}

.hero-content {
  position: relative;
  z-index: 1;
}



.hero-content {
  position: relative;
  z-index: 1;
}


.hero-content {
  max-width: 700px;
  margin: 0 auto;
}

.hero-content h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.hero-content p {
  font-size: 1.1rem;
  margin-bottom: 30px;
}

.search-bar {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}

.search-bar input[type="text"] {
  padding: 12px 16px;
  font-size: 1rem;
  border: none;
  border-radius: 6px;
  width: 70%;
  max-width: 400px;
  outline: none;
}

.search-bar button {
  padding: 12px 20px;
  font-size: 1rem;
}

.event-detail-card {
  background: #fff;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  display: flex;
  gap: 32px;
  padding: 32px;
  margin: 32px;
  flex-wrap: wrap;
}

.event-detail-card img {
  width: 100%;
  max-width: 360px;
  height: 240px;
  object-fit: cover;
  border-radius: var(--radius);
}

.event-info {
  flex: 1 1 240px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

@media (max-width: 768px) {
  .event-detail-card {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .event-info {
    align-items: center;
  }
}


  </style>
</head>

<body>
  <nav class="navbar">
    <div class="container">
      <a class="navbar-brand" href="/">
        <img src="/static/img/logo.png" alt="Tá Marcado Logo" style="height: 36px;" />
        Tá Marcado
      </a>

      <button class="navbar-toggler" id="navToggle" aria-label="Abrir menu">&#9776;</button>

      <div class="collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item"><a class="nav-link" href="/events">Eventos</a></li>
          <li class="nav-item"><a class="nav-link" href="/login">Login</a></li>
          <li class="nav-item"><a class="nav-link" href="/users/add">Cadastrar</a></li>
        </ul>
      </div>
    </div>
  </nav>

  {{!base}}

  <footer>
    <p>&copy; 2025 – Tá Marcado. Todos os direitos reservados.</p>
  </footer>

  <script>
    document.getElementById('navToggle').addEventListener('click', () => {
      document.getElementById('navbarNav').classList.toggle('show');
    });
  </script>
</body>

</html>
