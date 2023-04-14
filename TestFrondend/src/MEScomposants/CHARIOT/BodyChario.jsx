import React from 'react';

const BodyChariot= () =>{
    return(
<span>

   
    <div className="cart-section mt-150 mb-150">
      <div className="container">
        <div className="row">
          <div className="col-lg-8 col-md-12">
            <div className="cart-table-wrap">
              <table className="cart-table">
                <thead className="cart-table-head">
                  <tr className="table-head-row">
                    <th className="product-remove"></th>
                    <th className="product-image">Image du produit </th>
                    <th className="product-name">Nom</th>
                    <th className="product-price">Prix</th>
                    <th className="product-quantity">Quantit</th>
                    <th className="product-total">Total</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="table-body-row">
                    <td className="product-remove">
                      <a href="#"><i className="far fa-window-close"></i></a>
                    </td>
                    <td className="image1">
                     
                    </td>
                    <td className="product-name">Fraise</td>
                    <td className="product-price">2.400 francs</td>
                    <td className="product-quantity">
                      <input type="number" placeholder="0" />
                    </td>
                    <td className="product-total">1</td>
                  </tr>
                  <tr className="table-body-row">
                    <td className="product-remove">
                      <a href="#"><i className="far fa-window-close"></i></a>
                    </td>
                    <td className="image2">
                     
                    </td>
                    <td className="product-name">Baie</td>
                    <td className="product-price">2.400 francs</td>
                    <td className="product-quantity">
                      <input type="number" placeholder="0" />
                    </td>
                    <td className="product-total">1</td>
                  </tr>
                  <tr className="table-body-row">
                    <td className="product-remove">
                      <a href="#"><i className="far fa-window-close"></i></a>
                    </td>
                    <td className="image3">
                      
                    </td>
                    <td className="product-name">Lemon</td>
                    <td className="product-price">1.000 francs</td>
                    <td className="product-quantity">
                      <input type="number" placeholder="0" />
                    </td>
                    <td className="product-total">1</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <div className="col-lg-4">
            <div className="total-section">
              <table className="total-table">
                <thead className="total-table-head">
                  <tr className="table-total-row">
                    <th>Total</th>
                    <th>prix</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="total-data">
                    <td><strong>total: </strong></td>
                    <td>25.000francs</td>
                  </tr>
                  <tr className="total-data">
                    <td><strong>Expédition: </strong></td>
                    <td>$45</td>
                  </tr>
                  <tr className="total-data">
                    <td><strong>Total: </strong></td>
                    <td>1.000francs</td>
                  </tr>
                </tbody>
              </table>
              <div className="cart-buttons">
                <a href="cart.html" className="boxed-btn">mise ajour panier</a>
                <a href="checkout.html" className="boxed-btn black">vérifier</a>
              </div>
            </div>

            <div className="coupon-section">
              <h3>Appliquer Coupon</h3>
              <div className="coupon-form-wrap">
                <form action="index.html">
                  <p><input type="text" placeholder="Coupon" /></p>
                  <p><input type="submit" value="Apply" /></p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
</span>
    );
}

export default BodyChariot;
