
import "./login.css"
export default function Login()
{
    return(
        <>
         <form action="" method="post">

            <input type="text" placeholder="firstname" name="fname"/><br/>
            <input type="text" placeholder="lastname" name="lname"/><br/>
            <input type="text" placeholder="Username" name="username"/><br/>
            <input type="email" placeholder="email" name="email"/><br/>
            <input type="password" name="pass-1"/><br/>
            <input type="password" name="pass-2"/><br/>
            <button type="submit">Submit</button>
        </form>
     </>

    ) ;
}