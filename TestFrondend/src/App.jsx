import { useState } from 'react'

// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
import Accueil from './MEScomposants/index'
import Liaison from './MEScomposants/newsPage/liaison'
import Shop from './MEScomposants/restaurant/shop'
function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      
  <Liaison/> 

    </div>
  );
}

export default App
