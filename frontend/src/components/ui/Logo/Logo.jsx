import logo from "../../../assets/logo-estudemais.svg";

function Logo({ className = "h-[42px]" }) {
  return <img src={logo} alt="EstudeMais" className={`block ${className}`} />;
}

export default Logo;
