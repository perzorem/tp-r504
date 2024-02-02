import java.io.*;
import org.apache.http.HttpEntity;
import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;

public class Client1
{
	public static void main(String[] args) 
	{	
		try
		{
			if (args.length == 0) 
			{
            	System.out.println("at least one arguments required");
 				System.exit(1);       	
			} 
           	System.out.println("Arguments number : " + args.length);
           	System.out.println("Given Arguments :");
           
           	for (int i = 0; i < args.length; i++) 
			{
               	System.out.println("Argument " + (i + 1) + ": " + args[i]);
			}
			CloseableHttpClient client = HttpClients.createDefault();
			String url = " http ://" + args[0];
			HttpGet request = new HttpGet (url);

			System . out . println ( " Executing request " + request.getRequestLine ( ) ) ;
			CloseableHttpResponse resp = client . execute ( request ) ;

			System . out . println ( "Response Line : " + resp . getStatusLine ( ) ) ;
			System . out . println ( "Response Code: " + resp . getStatusLine ( ) . getStatusCode ( ) ); 

            
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
	}
}