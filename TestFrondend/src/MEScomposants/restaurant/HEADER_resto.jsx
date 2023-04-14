import React from 'react';
import { Link } from 'react-router-dom';


const HEADER2 = () =>{
  return (
   
      <header className='tete'>
	
			
	<div className="top-header-area" id="sticker">
		<div className="container">
			<div className="row">
				<div className="col-lg-12 col-sm-12 text-center">
					<div className="main-menu-wrap">
						
						<div className="site">
							<a href="index.html"  >
								<div className="logo"></div>
								{/* <img src="./assets/static/img/logo.png" alt="weretryt"/> */}
							</a>
						</div>
						
						<nav className="main-menu">
							<ul>
							<li><a className="navbar-brand"> <Link to="/">Accueil</Link></a></li>
							<li> <Link to="/CONTACT/Contact">Contact</Link></li>


								<li> <Link to="/restaurant/shop">Restaurant</Link></li>
										
								<li> <Link to="/CHARIOT/chariot">Chariot</Link></li>

								<li><Link to="/connexion/login">Sign in</Link>
										<ul>
											<li> <Link to="/connexion/login">Sign in client </Link></li>
										    <li> <Link to="/connexion/loginRESTO">Sign in restaurant</Link></li>
										</ul>
								</li>
								<li>
									<div className="header-icons">
										<a className="shopping-cart" href="{% url 'cart' %}"><i className="fas fa-shopping-cart"></i></a>
										<a className="mobile-hide search-bar-icon" href="#"><i className="fas fa-search"></i></a>
									</div>
								</li>
							</ul>
						</nav>
						<a className="mobile-show search-bar-icon" href="#"><i className="fas fa-search"></i></a>
						<div className="mobile-menu"></div>
					
					</div>
				</div>
			</div>
		</div>
	</div>
	
				<div className="search-area">
					<div className="container">
						<div className="row">
							<div className="col-lg-12">
								<span className="close-btn"><i className="fas fa-window-close"></i></span>
								<div className="search-bar">
									<div className="search-bar-tablecell">
										<h3>Search For:</h3>
										<input type="text" placeholder="Keywords"/>
										<button type="submit">Search <i className="fas fa-search"></i></button>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			
				<div className="breadcrumb-section breadcrumb-bg">
		<div className="container">
			<div className="row">
				<div className="col-lg-8 offset-lg-2 text-center">
					<div className="breadcrumb-text">
						<p>FRAIS ET BIO</p>
						<h1>Restaurants</h1>
					</div>
				</div>
			</div>
		</div>
	</div>
	
 



</header>
 
  );
}

export default HEADER2;
