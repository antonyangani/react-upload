import React from 'react';

export default function FileUploadForm( props ) {
    return (
    <div>
        <form encType="multipart/form-data" action="#" className="p-10 bg-grey-400">
            <input type="file" name="fileName" onChange={props.uploader}></input>
        </form>
    </div> 
    )
}
