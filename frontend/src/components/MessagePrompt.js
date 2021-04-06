import React from 'react'

export default function MessagePrompt( props ) {
    return (
    <div>
        <h1 className='p-10 bg-grey-100'>{props.message}</h1>
    </div>
    )
}
