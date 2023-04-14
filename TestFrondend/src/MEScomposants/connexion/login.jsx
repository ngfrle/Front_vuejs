import React from 'react'
import LoginForm from '../connexion/loginCLIENT'




// import { ReactComponent as Logo } from '../assets/img/logo.svg'
// import Account_side from './elements/Account_sidbar'
const Login = () => {
  return (
    <header>
      <div className="art">
        {/* < RegistrationForm/> */}
        </div>

      <div className="art">
      <LoginForm/>
      </div>
      <div>
      {/* <PasswordResetForm/>  */}
       </div>
    </header>
  )
}

export default Login;
