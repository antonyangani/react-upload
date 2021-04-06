import Hero from './components/Hero'
import FileUpload from './components/FileUpload'
import Nav from './components/Nav';
import {useEffect, useState } from 'react';
import axios from 'axios';


function App() {

  
  const [user, setUser] = useState({})
  const base_url = "http://localhost:8000/api/"

  // setEffect allows for updating state 
  // set state takes two arguments, a FUNCTION and []. If the lattter is left blank the setEffect func runs only once

  useEffect( () => {
      async function fetchData(){
          const rq = await axios.get(base_url)
          setUser(rq.data)
      }
      fetchData()
  }, [base_url])

  return (
    <div>
      <div className='pb-5'>
          <Nav user={user}/>
      </div>
      
        <div className="max-w-5xl mx-auto bg-blue-50 mb-12">
          <div className="bg-white lg:flex lg:shadow-lg lg:rounded">
            <header className="App-header">
              <Hero />
              <FileUpload />
            </header>
          </div>
        </div>
    </div>
  );
}

export default App;
