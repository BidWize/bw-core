import React,{useState, useEffect} from "react"
import api from "./api"

const App =()=>{
  
  const[auctions,setAuctions] = useState([]);
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    start_time: "",
    end_time: ""
  });
  const fetchAuctions = async () => {
    const response = await api.get('/auctions');
    setAuctions(response.data);
  } 

  useEffect(() =>{
    fetchAuctions();
  }, []);

  const FormSubmit = async (event) =>{
    event.preventDefault();
    await api.post('/auctions',formData);
    fetchAuctions();
    setFormData({
      title: "",
      description: "",
      start_time: "",
      end_time: ""
    });


  }
  
}

export default App;
