import { useEffect, useState } from "react";
import { getElements } from "../api/elements_api";

export function ElementsList() {

    const [elements, setElements] = useState([]);

    useEffect(() => {
        async function getElementsData() {
            const res = await getElements();
            console.log(res);
            setElements(res);
        }
        getElementsData();
    }, []);
    return (
        <div>
            <ul>
                {elements.map(element => (
                    <li key={element.atomic_number}>{element.name} - {element.symbol}</li>
                ))}
            </ul>
        </div>
    );
}