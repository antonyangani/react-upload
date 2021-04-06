import React, { Component } from 'react'
import axios from 'axios'
import MessagePrompt from './MessagePrompt';
import FileUploadForm from './FileUploadForm';



class FileUpload extends Component {
    constructor( props ){
        super( props );
        this.state = {
            uploadStatus: null
        }

    };

    FileUploadFunction = ( event ) => {
        let uploadedFile = event.target.files[0]
        let form_data = new FormData();
        form_data.append('files', uploadedFile)
        axios.post('http://localhost:8000/api/upload/', form_data).then( response =>{
            this.setState({ uploadStatus: response.data })
        })

    };

    contentOrchastrator(){
        if( this.state.uploadStatus === null ) {
            return <FileUploadForm uploader={this.FileUploadFunction}/>
        }
        else {
            return <MessagePrompt message={(this.state.uploadStatus.msg === 'success') ? "The file upload was a success" : "There was an error `{this.state.uploadStatus.msg}`"} />
        }

    };
    render(){
        return(
            <div>
                { this.contentOrchastrator() }
            </div>
        )
        
    };

}

export default FileUpload;

