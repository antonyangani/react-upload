import React from 'react'
import { Link } from 'react-router-dom';


export default function Nav( props ) {

    return (
        <nav className='flex justify-between items-center h-16 bg-blue-50 text-black relative font-mono' role='navigation'>
            <Link to='/'>
                Angani CMS
            </Link>
            <div className='px-4 cursor-pointer md:hidden'>
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" /></svg>
            </div>
            <div className='pr-8 md:block hidden'>
                <Link className='p-1 px-5' to='/'>Home</Link>
                <Link className='p-1 px-5' to='/menu'>Menu</Link>
                <Link className='p-1 px-5' to='/about'>About</Link>
                <Link className='p-1 px-5' to='/contact'>Contact</Link>
                <Link className='p-1 px-5' to='/user'>{(props.user.fname) ? props.user.fname : 'Login'}</Link>
            </div>
        </nav>

    )
}
